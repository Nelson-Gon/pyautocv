# import relevant libraries
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.io import imread_collection
import numpy as np


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
            images_list=imread_collection("./*.jpg")
        else:
            images_list=imread_collection(self.directory + "/*.jpg")

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

    def convert_thresholded(self):
        """

        :return: Converts images from thresholding to a shape suitable for viewing

        """
        converted_images = []
        for original, binary in zip(self.gray_images(), self.threshold()):
            converted_images.append(binary.reshape(original.shape[0], original.shape[1]))

        return converted_images

    def detect_edges(self, operator):
        """

        :param operator: One of sobel_vertical, sobel_horizontal or laplace. Kernels used are available here:
        https://en.wikipedia.org/wiki/Sobel_operator
        :return: Edge detection using sobel vertical, sobel horizontal or laplace. Uses images that have already been
        thresholded

        """
        if operator not in ["sobel_horizontal", "sobel_vertical", "laplace"]:
            raise ValueError("operator should be one of sobel_vertical, sobel_horizontal or laplace")

        if operator == "sobel_horizontal":
            print("Using horizontal sobel")
            kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

        elif operator == "sobel_vertical":
            print("Using vertical sobel")
            kernel = np.array([[-1, 0, 1], [-2, 0, 2],  [-1, 0, 1]])

        else:
            print("Using laplace")
            kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

        return ndimage.convolve(self.convert_thresholded(), kernel, mode="reflect")

    def show_images(self,  thresholded=False, image_type="gray", nrows=1, ncols=2):
        """
      :param image_type: gray or colored. Defaults to gray
     :param nrows Number of rows to use on plot
     :param ncols Number of columns to use on plot
     :param thresholded Boolean, defaults to False
     :type nrows int
     :type ncols int
     :type thresholded bool

    """
        if self.read_images() is None:
            raise ValueError("A list of images is required.")

        if image_type not in ["colored", "gray"]:
            raise ValueError("Image type should be one of gray or colored.")

        plt_cmap = "viridis"

        if thresholded:
            image_list = self.detect_edges()
            plt_cmap = plt.gray()

        if image_type == "gray" and not thresholded:
            image_list = self.gray_images()

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
        for ind, image in enumerate(image_list):
            axes.ravel()[ind].imshow(image_list[ind], cmap=plt_cmap)
            axes.ravel()[ind].set_axis_off()
