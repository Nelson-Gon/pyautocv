# import relevant libraries
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.io import ImageCollection
from os import pathsep
import numpy as np
from itertools import chain


# init class segmentation
class Segmentation(object):
    def __init__(self, directory=None):
        """

        :param directory: A directory containing images(currently only supports .jpg images
        :type directory: str

        """
        self.directory = directory

    def read_images(self):
        """

        :return: Returns a multidimensional array containing arrays that represent images in a directory

        """
        # read png and jpg from current directory
        images_list = ImageCollection("./*.jpg" + pathsep + "./*.png")
        if self.directory is not None:
            images_list = ImageCollection(self.directory + "/*.jpg" + pathsep + "/*.png")

        return list(images_list)

    def gray_images(self):
        """

        :return: Returns grayed images. Currently supports only blue-green-red to gray conversion

        """
        return list(map(lambda x: cv2.cvtColor(x, cv2.COLOR_BGR2GRAY), self.read_images()))

    def smooth(self, mask="box", sigma=3, kernel_shape=(3, 3)):
        """

        :param sigma: Sigma to use for a gaussian filter
        :param mask: A low pass filter method to use for noise reduction
        :param kernel_shape: A tuple specifying the shape of the kernel. Defaults to (3, 3)
        :return: Images convolved with a low pass filter to reduce noise

        """
        image_list = self.read_images()
        mask_list = {'gaussian': lambda x: ndimage.gaussian_filter(x, sigma=sigma),
                     'box': lambda x: cv2.blur(x, ksize=kernel_shape),
                     'median': lambda x: cv2.medianBlur(x, ksize=kernel_shape)}
        # alias box with mean, would be great to have a .alias method
        mask_list.update({"mean": mask_list['box']})
        # convolve images with low pass filter
        low_pass_filtered = list(map(mask_list[mask], image_list))

        return low_pass_filtered


class Threshold(Segmentation):
    def __init__(self, directory, threshold_method):
        super().__init__(directory)
        self.directory = directory
        self.threshold_method = threshold_method

    def threshold_images(self, threshold_method="binary", use_threshold=127, use_max=255):
        """

        :param threshold_method:
        :param use_threshold:
        :param use_max:
        :return:
        :return: Converts images from thresholding to a shape suitable for viewing

        """
        # use cv2's threshold instead since this is more mature, don't reinvent
        # There must be a different way than a list-map approach
        self.threshold_method = threshold_method
        threshold_methods = {'binary': lambda x: cv2.threshold(x, use_threshold, use_max, cv2.THRESH_BINARY),
                             'binary_inverse': lambda x: cv2.threshold(x, use_threshold, use_max,
                                                                       cv2.THRESH_BINARY_INV),
                             'thresh_to_zero': lambda x: cv2.threshold(x, use_threshold, use_max,
                                                                       cv2.THRESH_TOZERO),
                             'otsu': lambda x: cv2.threshold(x, use_threshold, use_max,
                                                             cv2.THRESH_BINARY + cv2.THRESH_OTSU)}
        image_list = self.gray_images()

        thresholded_images = list(map(threshold_methods[threshold_method], image_list))
        # drop ret val
        thresholded_images = [image[1] for image in thresholded_images]

        return thresholded_images


class EdgeDetection(Segmentation):

    def __init__(self, directory, operator):
        super().__init__(directory)
        self.directory = directory
        self.operator = operator

    # need
    def available_operators(self):
        available_operators = ["sobel_horizontal", "sobel_vertical", "prewitt_horizontal", "prewitt_vertical",
                               "laplace", "roberts_vertical", "roberts_horizontal", "scharr_vertical",
                               "scharr_horizontal"]
        return available_operators

    def detect_edges(self, operator="sobel_vertical", kernel_size=3, **kwargs):
        """

        :param kernel_size: int size to use for edge detection kernels
        :param kernel_shape: tuple Shape to use for kernel smoothing
        :param operator: One of sobel_vertical, sobel_horizontal,prewitt_horizontal,prewitt_vertical or laplace.
        Kernels used are available here: https://en.wikipedia.org/wiki/Sobel_operator
        :return: Edge detection using sobel vertical, sobel horizontal or laplace. Uses images that have already been
        thresholded

        """
        self.operator = operator
        self.kernel_size = kernel_size

        if operator not in self.available_operators():
            raise ValueError("operator should be one of {}".format(self.available_operators()))

        kernels = {'sobel_horizontal': lambda x: cv2.Sobel(x, cv2.CV_64F, 1, 0, ksize=self.kernel_size),
                   'sobel_vertical': lambda x: cv2.Sobel(x, cv2.CV_64F, 0, 1, ksize=self.kernel_size),
                   'roberts_horizontal': lambda x: ndimage.convolve(x, np.array([[1, 0], [0, -1]]), mode="reflect"),
                   'roberts_vertical': lambda x: ndimage.convolve(x, np.array([[0, 1], [-1, 0]]), mode="reflect"),
                   'laplace': lambda x: cv2.Sobel(x, cv2.CV_64F, 1, 0, ksize=self.kernel_size),
                   'prewitt_horizontal': lambda x: ndimage.convolve(x, np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]),
                                                                    mode="reflect"),
                   'prewitt_vertical': lambda x: ndimage.convolve(x, np.array([[1, 1, 1], [0, 0, 0],
                                                                               [-1, -1, -1]]),
                                                                  mode="refelct"),
                   'scharr_horizontal': lambda x: ndimage.convolve(x,
                                                                   np.array([[3, 0, -3], [10, 0, -10], [3, 0, -3]]),
                                                                   mode="reflect"),
                   'scharr_vertical': lambda x: ndimage.convolve(x,
                                                                 np.array([[3, 10, 3], [0, 0, 0], [-3, -10, -3]]),
                                                                 mode="reflect")}

        print("Using {}".format(self.operator))

        final_images = list(map(kernels[self.operator], self.smooth(**kwargs)))

        return final_images


def show_images(original_images=None, processed_images=None):
    """
    :param original_images: Original Images from read_images()
    :param processed_images: Images that have been converted eg from detect_edges()
    """
    # need to figure out how any works in python
    if original_images is None or processed_images is None:
        raise ValueError("Both original and processed image lists are required.")

    image_list = list(chain(original_images, processed_images))

    if len(image_list) % 2 == 0:
        ncols = len(image_list) / 2
    else:
        ncols = len(image_list)

    fig, axes = plt.subplots(nrows=2, ncols=int(ncols))

    for ind, image in enumerate(image_list):
        axes.ravel()[ind].imshow(image_list[ind])
        axes.ravel()[ind].set_axis_off()
