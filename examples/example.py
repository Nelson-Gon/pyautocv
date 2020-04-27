from pyautocv.segmentation import *
images_list=Segmentation("images")
images_list.show_images(thresholded=False)
images_list.show_images(thresholded=True,operator="laplace")

