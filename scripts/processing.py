if __name__ == "__main__":
    from pyautocv.segmentation import *
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--directory", type=str, help="Path to directory containing images",
                            required=True)
    arg_parser.add_argument("-s", "--suffix", type=str, help="Format of images to load", required=True)
    arg_parser.add_argument("-o", "--operation", type=str, help="Type of processing to perform", required=True)
    arg_parser.add_argument("-mt", "--max-threshold", type=int, help="Maximum threshold for thresholding", required=False)
    arg_parser.add_argument("-t", "--threshold", type=int, help="Threshold if thresholding", required=False)
    arg_parser.add_argument("-m", "--method", type=str, help="Threshold/Edge Detection/Smoothing method", required=False)
    arg_parser.add_argument("-k", "--kernel-size", type=int, nargs="+",
                            help="Kernel Size/Shape. Int for edge detection, tuple for smoothing")
    # Switch statement based on target operation
    arguments = arg_parser.parse_args()
    init_call = Segmentation(arguments.directory, image_suffix=arguments.suffix)
    call_methods = {"detect_edges": init_call.detect_edges,
                    "threshold": init_call.threshold_images,
                    "smooth": init_call.smooth}
    show_images(init_call.read_images(), call_methods[arguments.operation]())
    plt.show()

