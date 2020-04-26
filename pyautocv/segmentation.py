# import relevant libraries
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.io import imread_collection
import numpy as np

# read relevant images
# image source
def read_images(directory=None):
    if directory is None:
        return imread_collection("./*.jpg")
    else:
        return imread_collection(directory + "/*.jpg")






# change images to gray scale
# aim: Detect the two cell types, shown here as red and yellow
# Convert to a single channel

def gray_images(image_list):
    return list(map(lambda x: cv2.cvtColor(x,cv2.COLOR_BGR2GRAY),image_list))

# define thresholding methods

def threshold(image_list,type="simple"):
    # find image shapes
    image_list = gray_images(image_list)
    image_shapes = [x.shape for x in image_list]
    reshaped_images = []
    final_images = []
    if type=="simple":
        # simple thresholding: get pixel mean, use as threshold
        for shape, image in zip(image_shapes, image_list):
            reshaped_images.append(image.reshape(shape[0] * shape[1]))
        for reshaped_image in reshaped_images:
                final_images.append(np.where(reshaped_image > reshaped_image.mean(), 1, 0 ))
        return final_images




def convert_thresheld(thresheld_images, original_images):
    original_images = gray_images(original_images)
    converted_images = []
    for original, binary in zip(original_images, thresheld_images):
        converted_images.append(binary.reshape(original.shape[0], original.shape[1]))
    return converted_images




def detect_edges(sobel_operator, image):
    # can use multiple thresholds too
    # detect edges(discontinuity)
    # weight matrix, element wise multiply with image, output
    # convolve
    # sobel operator [1 2 1, 000, -1,-2,-1] -> horizontal [-1 0 1, -2 0 2, -1 0 1] -> vertical
    # define sobel operators

    if sobel_operator not in ["horizontal", "vertical", "laplace"]:
        raise ValueError("sobel_operator should be one of vertical, horizontal or laplace")
    if sobel_operator == "horizontal":
        print("Using horizontal sobel")
        sobel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    elif sobel_operator == "vertical":
        print("Using vertical sobel")
        sobel = np.array([[-1, 0, 1], [-2, 0, 2],
                          [-1, 0, 1]])
    else:
        print("Using laplace")
        sobel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

    return ndimage.convolve(image, sobel, mode="reflect")



def show_images(image_list=None, thresheld=False, image_type="gray", nrows=1, ncols=1):
    """
    :param image_type: gray or colored. Defaults to gray
    :param image_list: A list of images
    :param nrows Number of rows to use on plot
    :param ncols Number of columns to use on plot
    :type nrows int
    :type ncols int
    :type image_list: list
    :type image_type: str
    """
    if image_list is None:
        raise ValueError("A list of images is required.")
    if image_type not in ["colored", "gray"]:
        raise ValueError("Image type should be one of gray or colored.")
    plt_cmap ="viridis"

    if thresheld:
        image_list = image_list
        plt_cmap=plt.gray()

    if image_type=="gray" and not thresheld:
        image_list = gray_images(image_list)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
    for ind, image in enumerate(image_list):
        axes.ravel()[ind].imshow(image_list[ind], cmap=plt_cmap)
        axes.ravel()[ind].set_axis_off()





