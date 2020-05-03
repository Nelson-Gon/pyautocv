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

    def threshold(self, threshold_method="simple"):

        """

        :param threshold_method: a string to specify the kind of thresholding to use. simple for mean thresholding
        :return: Thresholded images.

        """
        image_list = self.gray_images()
        image_shapes = [x.shape for x in image_list]
        reshaped_images = []
        final_images = []
        # simple thresholding: get pixel mean, use as threshold
        if threshold_method == "simple":
            for shape, image in zip(image_shapes, image_list):
                reshaped_images.append(image.reshape(shape[0] * shape[1]))
            for reshaped_image in reshaped_images:
                final_images.append(np.where(reshaped_image > reshaped_image.mean(), 1, 0))

        return final_images

    def convert_thresholded(self, threshold_method="simple"):
        """

        :return: Converts images from thresholding to a shape suitable for viewing

        """
        converted_images = []
        for original, binary in zip(self.read_images(), self.threshold(threshold_method)):
            converted_images.append(binary.reshape(original.shape[0], original.shape[1]))

        return converted_images

    def detect_edges(self, operator="laplace",threshold_method="simple"):
        """

        :param threshold_method: method to threshold with
        :param operator: One of sobel_vertical, sobel_horizontal,prewitt_horizontal,prewitt_vertical or laplace. Kernels used are available here:
        https://en.wikipedia.org/wiki/Sobel_operator
        :return: Edge detection using sobel vertical, sobel horizontal or laplace. Uses images that have already been
        thresholded

        """
        available_operators = ["sobel_horizontal", "sobel_vertical","prewitt_horizontal","prewitt_vertical",
                               "laplace", "roberts_vertical", "roberts_horizontal"]
        if operator not in available_operators:
            raise ValueError("operator should be one of {}".format(available_operators))

        kernels = {'sobel_horizontal': np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]),
                   'sobel_vertical': np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
                   'roberts_horizontal': np.array([[1, 0], [0, -1]]), 'roberts_vertical': np.array([[0, 1], [-1, 0]]),
                   'laplace': np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]),
                   'prewitt_horizontal': np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]),
                   'prewitt_vertical': np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]),
                   'scharr_horizontal': np.array([[3, 0, -3], [10, 0, -10],[3,0, -3]]),
                   'scharr_vertical': np.array([[3, 10, 3], [0, 0, 0], [-3, -10, -3]])}

        print("Using {}".format(operator))

        final_images = []

        for image in self.convert_thresholded(threshold_method):
            final_images.append(ndimage.convolve(image, kernels[operator], mode="reflect"))

        return final_images

    def show_images(self, nrows=2, ncols=2, operator="sobel_vertical",
                    threshold_method="simple"):
        """


     :param threshold_method:
     :param nrows Number of rows to use on plot
     :param ncols Number of columns to use on plot
     :param operator: operator to detect_edges
     :type nrows int
     :type ncols int
     :type thresholded bool

    """
        if self.read_images() is None:
            raise ValueError("A list of images is required.")


        #plt_cmap = "viridis"

        image_list = list(chain(self.read_images(),self.detect_edges(operator=operator,
                                                                     threshold_method=threshold_method)))


        fig, axes = plt.subplots(nrows=nrows, ncols=ncols)

        for ind, image in enumerate(image_list):
                axes.ravel()[ind].imshow(image_list[ind])
                axes.ravel()[ind].set_axis_off()
