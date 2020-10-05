if __name__ == "__main__":
    from pyautocv.segmentation import *
    test_list = Segmentation("images/cats", image_suffix="png")
    show_images(test_list.read_images(), test_list.threshold_images(threshold_method="binary_inverse"))
    plt.show()
