from pyautocv.segmentation import *
import os

os.chdir("pyautocv")
# gray images
images_list = Segmentation("images/cats")
show_images(gray_images(images_list.read_images()), images_list.read_images())
# smooth images
show_images(images_list.read_images(), images_list.smooth())
# use median
show_images(images_list.read_images(), images_list.smooth(mask="median", kernel_shape=(7, 7)))

# detect edges

show_images(images_list.read_images(), images_list.detect_edges(operator="roberts", mask="gaussian", sigma=0.8))

show_images(images_list.read_images(), images_list.detect_edges(operator="laplace", mask="gaussian", sigma=0.8))

# threshold
cats = Segmentation("images/cats")
show_images(cats.read_images(), cats.threshold_images(threshold_method="binary_inverse"))

# biology
to_threshold = Segmentation("images/biology")
show_images(to_threshold.read_images(), to_threshold.threshold_images())
show_images(to_threshold.read_images(), to_threshold.threshold_images(threshold_method="otsu"))
# houses
images_list = Segmentation("images/houses")

show_images(images_list.read_images(), images_list.threshold_images(threshold_method="thresh_to_zero"))
# random
images_list = Segmentation("images")
show_images(images_list.read_images(), images_list.detect_edges())

# potholes
images_list = Segmentation("images/potholes")

show_images(images_list.read_images(), images_list.threshold_images("binary"))
