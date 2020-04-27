from pyautocv.segmentation import *
images_list=Segmentation("images/biology")
images_list.show_images(thresholded=True,ncols=3,operator="sobel_horizontal")
images_list.show_images(thresholded=True,ncols=3,operator="prewitt_horizontal")
images_list.show_images(thresholded=True,ncols=3,operator="prewitt_vertical")

# houses
images_list=Segmentation("images/houses")

images_list.show_images(thresholded=True,operator="prewitt_vertical")
# random
images_list=Segmentation("images")
images_list.show_images(thresholded=False,ncols=2)

#potholes
images_list=Segmentation("images/potholes")
images_list.show_images()
images_list.show_images(thresholded=True,ncols=2, operator="prewitt_vertical")