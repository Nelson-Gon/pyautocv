# import relevant libraries
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.io import imread_collection
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
        if self.directory is None:
            images_list = imread_collection("./*.jpg")
        else:
            images_list = imread_collection(self.directory + "/*.jpg")

        return list(images_list)

    def gray_images(self):
        """

        :return: Returns grayed images. Currently supports only blue-green-red to gray conversion

        """
        return list(map(lambda x: cv2.cvtColor(x, cv2.COLOR_BGR2GRAY), self.read_images()))

    def smooth(self, mask="box"):
        """

        :param mask: A low pass filter method to use for noise reduction
        :return: Images convolved with a low pass filter to reduce noise

        """
        image_list = self.gray_images()
        mask_list = {'box': 1 / 9 * np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])}
        # alias box with mean, would be great to have a .alias method
        mask_list.update({"mean": mask_list['box']})
        # convolve images with low pass filter
        low_pass_filtered = []
        for img in image_list:
            low_pass_filtered.append(ndimage.convolve(img, mask_list[mask], mode="reflect"))

        return low_pass_filtered


class Threshold(Segmentation):
    def __init__(self,directory,threshold_method):
        super().__init__(directory)
        self.directory=directory
        self.threshold_method=threshold_method

    def threshold(self, threshold_method="simple"):

        """

        :param threshold_method: a string to specify the kind of thresholding to use. simple for mean thresholding
        :return: Thresholded images.

        """
        self.threshold_method=threshold_method
        image_list = self.gray_images()
        image_shapes = [x.shape for x in image_list]
        reshaped_images = []
        final_images = []
        # simple thresholding: get pixel mean, use as threshold
        if self.threshold_method == "simple":
            for shape, image in zip(image_shapes, image_list):
                reshaped_images.append(image.reshape(shape[0] * shape[1]))
            for reshaped_image in reshaped_images:
                final_images.append(np.where(reshaped_image > reshaped_image.mean(), 1, 0))

        return final_images

    def threshold_images(self, threshold_method="simple"):
        """

        :return: Converts images from thresholding to a shape suitable for viewing

        """
        self.threshold_method=threshold_method
        converted_images = []
        for original, binary in zip(self.read_images(), self.threshold(self.threshold_method)):
            converted_images.append(binary.reshape(original.shape[0], original.shape[1]))

        return converted_images


class EdgeDetection(Segmentation):

    def __init__(self, directory, operator,mask):
        super().__init__(directory)
        self.directory = directory
        self.operator = operator
        self.mask = mask
        
    def available_operators(self):
        available_operators = ["sobel_horizontal", "sobel_vertical", "prewitt_horizontal", "prewitt_vertical",
                                    "laplace", "roberts_vertical", "roberts_horizontal", "scharr_vertical",
                                    "scharr_horizontal"]
        return available_operators

    def detect_edges(self,operator="sobel_vertical"):
        """

        :param mask: method to use for smoothing
        :param operator: One of sobel_vertical, sobel_horizontal,prewitt_horizontal,prewitt_vertical or laplace. Kernels used are available here:
        https://en.wikipedia.org/wiki/Sobel_operator
        :return: Edge detection using sobel vertical, sobel horizontal or laplace. Uses images that have already been
        thresholded

        """
        self.operator=operator

        if operator not in self.available_operators():
            raise ValueError("operator should be one of {}".format(self.available_operators()))

        kernels = {'sobel_horizontal': np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]),
                   'sobel_vertical': np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
                   'roberts_horizontal': np.array([[1, 0], [0, -1]]), 'roberts_vertical': np.array([[0, 1], [-1, 0]]),
                   'laplace': np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]),
                   'prewitt_horizontal': np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]),
                   'prewitt_vertical': np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]),
                   'scharr_horizontal': np.array([[3, 0, -3], [10, 0, -10], [3, 0, -3]]),
                   'scharr_vertical': np.array([[3, 10, 3], [0, 0, 0], [-3, -10, -3]])}

        print("Using {}".format(self.operator))

        final_images = []

        for image in super(EdgeDetection, self).smooth(mask=self.mask):
            final_images.append(ndimage.convolve(image, kernels[self.operator], mode="reflect"))

        return final_images


def show_images(original_images=None, processed_images=None, nrows=2, ncols=2):
    """


     :param original_images: Original Images from read_images()
     :param nrows Number of rows to use on plot
     :param ncols Number of columns to use on plot
     :param processed_images: Images that have been converted eg from detect_edges()
     :type nrows int
     :type ncols int
     :type mask str

    """
    # need to figure out how any works in python
    if original_images is None or processed_images is None:
        raise ValueError("Both original and processed image lists are required.")

    image_list = list(chain(original_images, processed_images))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)

    for ind, image in enumerate(image_list):
        axes.ravel()[ind].imshow(image_list[ind])
        axes.ravel()[ind].set_axis_off()
