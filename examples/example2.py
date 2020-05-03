from pyautocv.segmentation import *
edge_detection = EdgeDetection("images","sobel_vertical","box")
# smooth
to_smooth = EdgeDetection("images/people","sobel_vertical","box")
show_images(*[to_smooth.gray_images(), to_smooth.smooth()])

# detect edges

show_images(*[edge_detection.gray_images(), edge_detection.detect_edges()])

# use laplace
show_images(*[edge_detection.gray_images(), edge_detection.detect_edges(operator="laplace")])

# Thresholding

to_threshold = Threshold("images/flowers",threshold_method="simple")
show_images(to_threshold.gray_images(),to_threshold.threshold_images())