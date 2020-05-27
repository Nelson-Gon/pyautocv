import os
# need to automate this, "export" data
#os.getcwd() should change to pyautocv if not
os.chdir("pyautocv")
from pyautocv.segmentation import *
to_smooth = EdgeDetection("images/people","sobel_vertical")
show_images(to_smooth.gray_images(), to_smooth.smooth())
# detect edges
edge_detection = EdgeDetection("images","sobel_vertical")
show_images(edge_detection.read_images(), edge_detection.detect_edges(operator="laplace",mask="gaussian",sigma=3.5))

# Thresholding
to_threshold = Threshold("images/biology",threshold_method="binary")
show_images(to_threshold.read_images(),to_threshold.threshold_images())
# cats
to_threshold = Threshold("images/cats",threshold_method="binary")
show_images(to_threshold.read_images(),to_threshold.threshold_images(threshold_method="otsu"))
# potholes
to_threshold = Threshold("images/potholes",threshold_method="otsu")
show_images(to_threshold.read_images(),to_threshold.threshold_images())
# houses
to_threshold = Threshold("images/houses",threshold_method="binary_inverse")
show_images(to_threshold.read_images(),to_threshold.threshold_images())

# people
to_threshold = Threshold("images/people",threshold_method="binary_inverse")
show_images(to_threshold.read_images(),to_threshold.threshold_images())