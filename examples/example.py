from pyautocv.segmentation import *
import os
os.chdir("pyautocv")
# gray images
images_list = Segmentation("images/dic", image_suffix="tif", color_mode="gray")


# smooth images
show_images(images_list.read_images(), images_list.smooth())
# use median
show_images(images_list.read_images(), images_list.smooth(mask="median", kernel_shape=(7, 7)), number = 4)

# detect edges

show_images(images_list.read_images(), images_list.detect_edges(operator="roberts", mask="gaussian", sigma=0.8), number=4)

show_images(images_list.read_images(), images_list.threshold_images(), number = 4)

show_images(images_list.read_images(), images_list.threshold_images(threshold_method="otsu"), number = 4)

# threshold
cats = Segmentation("images/cats")
show_images(cats.read_images(), cats.threshold_images(threshold_method="binary_inverse"), number=4)

images_list_gray_mode=Segmentation("images/dic", image_suffix ="tif", color_mode = "gray")
# no need to gray them since they are already gray
show_images(images_list_gray_mode.read_images(), images_list_gray_mode.threshold_images(), number = 4)

# biology
to_threshold = Segmentation("images/biology")
show_images(to_threshold.read_images(), to_threshold.threshold_images(), number=4)
show_images(to_threshold.read_images(), to_threshold.threshold_images(threshold_method="otsu"), number = 4)
# houses
images_list = Segmentation("images/houses")

show_images(images_list.read_images(), images_list.threshold_images(threshold_method="thresh_to_zero"), number=4)
# random
images_list = Segmentation("images")
show_images(images_list.read_images(), images_list.detect_edges(), number=4)

# potholes
images_list = Segmentation("images/potholes")

show_images(images_list.read_images(), images_list.threshold_images("binary"), number=4)

# people
people = Segmentation("images/people")
show_images(people.read_images(), people.threshold_images(threshold_method="binary_inverse"), number=4)

images_list_gray_mode=Segmentation("images/dic", image_suffix ="tif", color_mode = "gray")
# no need to gray them since they are already gray
show_images(images_list_gray_mode.read_images(), images_list_gray_mode.threshold_images(), number = 4)

images_list=Segmentation("images/potholes")

show_images(images_list.read_images(), images_list.threshold_images("binary"))

images_list = Segmentation("images/cats")
show_images(images_list.read_images(), images_list.smooth(mask="median", kernel_shape=(7, 7)))
show_images(images_list.read_images(), images_list.detect_edges(operator="laplace", mask="gaussian", sigma=0))
images_list=Segmentation("images/cats")
show_images(images_list.smooth(), images_list.read_images(),number=2)
show_images(gray_images(images_list.read_images()), images_list.read_images(), number=2)
