if __name__ == "__main__":
    from pyautocv.segmentation import *
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--directory", type=str, help="Path to directory containing images",
                            required=True)
    arg_parser.add_argument("-s", "--suffix", type=str, help="Format of images to load", required=True)
    arg_parser.add_argument("-m", "--method", type=str, help="Threshold method to use", required=True)
    arguments = arg_parser.parse_args()
    test_list = Segmentation(arguments.directory, image_suffix=arguments.suffix)
    show_images(test_list.read_images(), test_list.threshold_images(threshold_method=arguments.method))
    plt.show()
