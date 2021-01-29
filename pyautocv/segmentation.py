# import relevant libraries
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.io import imread_collection, imread
from skimage.transform import resize
from skimage import filters
from os import pathsep, path
import numpy as np
from itertools import chain
import glob


def gray_images(images):
    """

    :param images: A list of color images that should be grayed/greyed.
    :return: Returns grayed images. Currently supports only blue-green-red to gray conversion

    """
    if not isinstance(images, list):
        raise TypeError(f"Expected a list of images not {type(images).__name__}")

    return list(map(lambda x: cv2.cvtColor(x, cv2.COLOR_BGR2GRAY), images))


class Segmentation(object):
    def __init__(self, directory=None, image_suffix="png", color_mode="rgb"):
        """

        :param directory: A directory containing images(currently only supports .jpg images
        :param image_suffix: Suffix of images in directory. For mixed types(png and jpg), set suffix as png. \
        Defaults to png.
        :param color_mode: Specifies the nature of input images. Defaults to rgb implying not grayscale
        :type directory: str
        :return: An object of class Segmentation

        """
        self.directory = directory
        if self.directory is None:
            self.directory = "."
        # check that the directory actually exists
        if not path.isdir(self.directory):
            raise NotADirectoryError(f"{self.directory} is not a valid directory in the current path.")

        self.image_suffix = image_suffix

        if self.image_suffix not in ["png", "jpg", "tif"]:
            raise ValueError("Only png, jpg, and tif are supported")

        self.color_mode = color_mode

    def read_images(self, other_directory=None):
        """
        :param other_directory: Use if images exist in sub-folders or another folder. Only for jpg and png suffixes.
        :return: Returns an n-D array of images.
        """

        if self.image_suffix == "tif":
            images_list = sorted(glob.glob(self.directory + "/*.tif"))
            return [imread(x, plugin='pil') for x in images_list]
        else:
            read_path = self.directory + "/*.jpg" + pathsep + self.directory + "/*.png"
            if other_directory is None:
                pass
            else:
                read_path = read_path + pathsep + other_directory + "/*.png" + pathsep + other_directory + "/*.jpg"
            return list(imread_collection(read_path))

    def smooth(self, mask="box", kernel_shape=(5, 5), **kwargs):
        """
        :param mask: A low pass filter method to use for noise reduction
        :param kernel_shape: A tuple specifying the shape of the kernel. Defaults to (3, 3)
        :return: Images convolved with a low pass filter to reduce noise
        """
        if mask not in ["mean", "gaussian", "box", "median"]:
            raise ValueError("mask should be one of mean, median, box, and gaussian")

        if not isinstance(kernel_shape, tuple):
            raise TypeError(f"Expected a tuple not {type(kernel_shape).__name__}")

        image_list = self.read_images()
        mask_list = {'gaussian': lambda x: ndimage.gaussian_filter(x, **kwargs),
                     'box': lambda x: cv2.blur(x, ksize=kernel_shape),
                     'median': lambda x: cv2.medianBlur(x, ksize=kernel_shape[0])}
        # alias box with mean, would be great to have a .alias method
        mask_list.update({"mean": mask})
        # convolve images with low pass filter
        print(f"Smoothing with {mask}")
        low_pass_filtered = list(map(mask_list[mask], image_list))

        return low_pass_filtered

    def threshold_images(self, threshold_method="binary", use_threshold=127, use_max=255):
        """

        :param threshold_method: Threshold method to use.
        :param use_threshold: Threshold value
        :param use_max: Maximum value of threshold
        :return: Thresholded images

        """
        # use cv2's threshold instead since this is more mature, don't reinvent
        # There must be a different way than a list-map approach
        threshold_methods = {'binary': lambda x: cv2.threshold(x, use_threshold, use_max, cv2.THRESH_BINARY),
                             'binary_inverse': lambda x: cv2.threshold(x, use_threshold, use_max,
                                                                       cv2.THRESH_BINARY_INV),
                             'thresh_to_zero': lambda x: cv2.threshold(x, use_threshold, use_max,
                                                                       cv2.THRESH_TOZERO),
                             'otsu': lambda x: cv2.threshold(x, use_threshold, use_max,
                                                             cv2.THRESH_BINARY + cv2.THRESH_OTSU)}
        # TODO
        # Automate key error messages
        # Support user defined methods

        if threshold_method not in threshold_methods.keys():
            raise ValueError(f"Thresholding with {threshold_method} is not supported")

        image_list = self.read_images()

        if self.color_mode == "rgb":
            image_list = gray_images(image_list)

        thresholded_images = list(map(threshold_methods[threshold_method], image_list))
        # drop ret val
        thresholded_images = [image[1] for image in thresholded_images]

        return thresholded_images

    def detect_edges(self, operator="sobel_vertical", kernel_size=3, optional_mask=None, **kwargs):
        """
        :param optional_mask: See skimage.filters.scharr_v for details.
        :param kernel_size: int size to use for edge detection kernels
        :param operator: One of sobel_vertical, sobel_horizontal,prewitt_horizontal,prewitt_vertical or laplace.
        :return: Detected edges
        """

        available_operators = ["sobel_horizontal", "sobel_vertical", "prewitt_horizontal", "prewitt_vertical",
                               "laplace", "roberts_cross_neg", "roberts_horizontal", "scharr_vertical",
                               "scharr_horizontal", "canny", "roberts"]

        if operator not in available_operators:
            raise ValueError(f"Edge detection with {operator} not supported.")

        kernels = {'sobel_horizontal': lambda x: cv2.Sobel(x, cv2.CV_64F, 1, 0, ksize=kernel_size),
                   'sobel_vertical': lambda x: cv2.Sobel(x, cv2.CV_64F, 0, 1, ksize=kernel_size),
                   'roberts': lambda x: filters.roberts(x, optional_mask),
                   'roberts_cross_neg': lambda x: ndimage.convolve(x, np.array([[0, -1], [1, 0]])),
                   'roberts_cross_pos': lambda x: filters.roberts_pos_diag(x, optional_mask),
                   'laplace': lambda x: cv2.Sobel(x, cv2.CV_64F, 1, 0, ksize=kernel_size),
                   'prewitt_horizontal': lambda x: filters.prewitt_h(x, optional_mask),
                   'prewitt_vertical': lambda x: filters.prewitt_v(x, optional_mask),
                   'scharr_horizontal': lambda x: filters.scharr_h(x, optional_mask),
                   'scharr_vertical': lambda x: filters.scharr_v(x, optional_mask)}

        print(f"Detecting edges with the {operator} operator")
        # denoise and gray

        if self.color_mode == "gray":
            denoised = self.smooth(**kwargs)
        else:
            denoised = gray_images(self.smooth(**kwargs))

        return list(map(kernels[operator], denoised))


def show_images(original_images=None, processed_images=None, cmap="gray", number=None, figure_size=(20, 20),
                custom_titles=None):
    """
    :param custom_titles: A list of length 2 for titles to use. Defaults to ['original','processed']
    :param figure_size: Size of the plot shown. Defaults to (20,20)
    :param original_images: Original Images from read_images()
    :param processed_images: Images that have been converted eg from detect_edges()
    :param cmap: Color cmap from matplotlib. Defaults to gray
    :param number: optional Number of images to show
    :return: A matplotlib plot of images
    """
    if number is None:
        # This assumes that both lists will be the same length
        # TODO: test for length equivalency, error on incompatible lengths
        number = len(original_images)

    image_list = reshape_images(original_images[:number])

    if custom_titles is None:
        custom_titles = ['original']

    if processed_images is not None:
        processed_images = reshape_images(processed_images[:number])
        image_list = list(chain(*zip(image_list, processed_images)))
        custom_titles = ["original", "processed"]

    # Currently only considering divisibility by three and two for image visualization
    # This is mostly necessary for single list visualization

    number_of_columns = len(image_list) / 3
    number_of_rows = 3

    if len(image_list) % 2 == 0:
        number_of_columns = len(image_list) / 2
        number_of_rows = 2

    custom_titles = custom_titles * len(image_list)

    fig, axes = plt.subplots(nrows=int(number_of_rows), ncols=int(number_of_columns), figsize=figure_size)

    print(f"Showing {number} image(s)")

    for ind, image in enumerate(image_list):
        axes.ravel()[ind].imshow(image, cmap=cmap)
        axes.ravel()[ind].set_title(f'{custom_titles[ind]}')
        axes.ravel()[ind].set_axis_off()


def resize_images(image_list=None, target_size=None):
    """

    :param image_list: A list of images or image that needs to be resized
    :param target_size: New target image size
    :return: Image or list of images that have been resized.


    """
    if image_list is None or target_size is None:
        raise ValueError("Please provide both an image list and a target size")

    if not isinstance(target_size, tuple):
        raise TypeError(f"Expected a tuple in target_size not {type(target_size).__name__}")

    return [resize(x, target_size) for x in image_list]


def reshape_images(image_list=None):
    """

    :param image_list: A list of images to reshape for plotting
    :return: Images that can be plotted with show_images

    """
    if image_list is None:
        raise ValueError("Please provide a list of images to reshape.")

    final_list = [img[:, :, 0] if len(img.shape) == 3 and img.shape[2] != 3 else img for img in image_list]
    return final_list


def stack_images(list_one=None, list_two=None, direction="horizontal"):
    """

    :param list_one: List containing image arrays to stack together
    :param list_two: Another list of image arrays
    :param direction: Stacking direction. One of horizontal and vertical,defaults to horizontal
    :return: Returns a list of images stacked together as requested.

    """
    if any(input_list is None for input_list in [list_one, list_two]):
        raise ValueError("Please provide two lists to stack")
    if not all(isinstance(input_list, list) for input_list in [list_one, list_two]):
        raise TypeError("Both list_one and list_two should be lists")
    if direction not in ["horizontal", "vertical", "h", "v"]:
        raise ValueError(f"direction should be one of horizontal, vertical, h, v not {direction}")
    stack_direction = {"horizontal": np.hstack, "vertical": np.vstack,
                       "h": np.hstack, "v": np.vstack}
    stacked_images = []
    for img_x, img_y in zip(list_one, list_two):
        stacked_images.append(stack_direction[direction]((img_x, img_y)))

    return stacked_images


def plot_hist(input_image=None, lim=None, color_mode="gray"):
    """

    :param input_image: An image representation(array) whose histogram is required.
    :param lim: A list to define the range of the x-axis, defaults to [0, 256]
    :param color_mode: One of gray or rgb. This determines the number of plots shown.
    :return: A histogram plot

    """
    if lim is None:
        lim = [0, 256]
    channel = "b"
    if color_mode == "rgb":
        channel = ('b', 'g', 'r')
    for i, col in enumerate(channel):
        calculated_hist = cv2.calcHist([input_image], [i], None, [256], [0, 256])
        plt.plot(calculated_hist, color=col)
        plt.xlim(lim)
