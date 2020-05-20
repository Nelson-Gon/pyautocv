from pyautocv.segmentation import *
to_smooth = EdgeDetection("images/people","sobel_vertical")
show_images(to_smooth.gray_images(), to_smooth.smooth())
# detect edges
edge_detection = EdgeDetection("images","sobel_vertical")
show_images(edge_detection.read_images(), edge_detection.detect_edges(operator="laplace",mask="gaussian",sigma=3.5))

# Thresholding

to_threshold = Threshold("images/biology",threshold_method="simple")
show_images(to_threshold.read_images(),to_threshold.threshold_images())

