from pyautocv.segmentation import *
# images root
images_list=Segmentation("images")
images_list.show_images()
images_list.show_images(operator="laplace")
# biology
images_list=Segmentation("images/biology")
len(images_list.read_images())
images_list.show_images(operator="sobel_horizontal",nrows=2,ncols=3)
images_list.show_images(operator="prewitt_horizontal", nrows=2, ncols=3)
images_list.show_images(operator="prewitt_vertical",nrows=2, ncols=3)

# houses
images_list=Segmentation("images/houses")

images_list.show_images(thresholded=True,operator="prewitt_vertical")
# random
images_list=Segmentation("images")
images_list.show_images()

#potholes
images_list=Segmentation("images/potholes")
images_list.show_images(operator="prewitt_vertical")

# flowers
images_list=Segmentation("images/test")
images_list.show_images(operator="prewitt_vertical")
