import os
# need to automate this, "export" data
#os.getcwd() should change to pyautocv if not
os.chdir("pyautocv")
from pyautocv.segmentation import *
edge_detection = Segmentation("images/cats")
show_images(edge_detection.read_images(), edge_detection.detect_edges(operator="laplace", mask="gaussian", sigma=0))
# Threshold
to_threshold = Segmentation("images/biology")
show_images(to_threshold.read_images(),to_threshold.threshold_images())
# threshold otsu
to_threshold = Segmentation("images/biology")
show_images(to_threshold.read_images(),to_threshold.threshold_images(threshold_method="otsu"))
# cats
to_threshold = Segmentation("images/cats")
show_images(to_threshold.read_images(),gray_images(to_threshold.read_images()))
to_threshold = Segmentation("images/people")
show_images(to_threshold.read_images(),to_threshold.detect_edges(operator="roberts"))

