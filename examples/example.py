from pyautocv.segmentation import *
images_list=Segmentation("images/biology")
images_list.show_images(thresholded=True,ncols=3,operator="sobel_horizontal")