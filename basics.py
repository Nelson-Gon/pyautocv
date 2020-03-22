# Reading an image
import cv2
# use imread to read in an image
original_img = cv2.imread("original_mountain.jpg")

# How is an image represented?
# multidimensional array of columns and rows of pixels
# each pixel has a value
import numpy as np
# create a square black image
img = np.zeros((3, 3), dtype = np.uint8)

# each pixel is a single 8-bit integer with values
# ranging between 0-255, 0 is black, 255 is white.
# everything inbetween is a shade of gray
# converting this image to a blue green image

img_bg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

img_bg

# each pixel now represented by a 3 element array.
# each integer represents one of the three color channels B,G,R.

# use imwrite to write images

# Convert between an image and raw bytes
# opencv image -- 2D or 3D array
# 24 bit BGR image -- 3D array

# create a bytearray of random bytes
import os

random_byte_array = bytearray(os.urandom(120000))

flat_np_array = np.array(random_byte_array)

gray_img = flat_np_array.reshape(300, 400)
cv2.imwrite('random_image.png', gray_img)
# convert to color
# need 3 * 3 for color
bgr_image = flat_np_array.reshape(100, 400, 3)
cv2.imwrite("random_img_color.png", bgr_image)
#cv2.imshow(bgr_image)

# accessing image data with np.array

#original_img[0, 0] = [255, 255, 255]
# try to read with load image
#cv2.imread("original_mountain.jpg", cv2.CV_L)
import matplotlib.pyplot as plt
#os.chdir("simplecv")
original_img = plt.imread("original_mountain.jpg")
# get image representation
img_copy = np.copy(original_img)
img_copy[0, 0] = [0, 0, 0]
# use itemset to modify the image
img_copy.itemset((150, 150, 0), 255)
img_copy.item(150, 150, 0)
# itemset faster than plain brute force indexing
# use slicing instead
img_copy[:, :, 1] = 0

cv2.imshow('image', img_copy)

# Uses of accessing pixels with numpy
# regions of interest(ROIs)
# define a given ROI and manipulate it
img_copy2 = np.copy(original_img)

my_roi = img_copy2[0: 200, 0:200]
img_copy2[300:500, 300:500] = my_roi
# essentially just transfers the roi from one point to another
cv2.imshow('image', img_copy2)