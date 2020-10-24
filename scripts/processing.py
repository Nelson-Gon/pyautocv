if __name__ == "__main__":
    from pyautocv.segmentation import *
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--directory", type=str, help="Path to directory containing images",
                            required=True)
    arg_parser.add_argument("-s", "--suffix", type=str, help="Format of images to load", required=True)
    arg_parser.add_argument("-o", "--operation", type=str, help="Type of processing to perform", required=True)
    arg_parser.add_argument("-mt", "--max-threshold", type=int, help="Maximum threshold for thresholding",
                            required=False)
    arg_parser.add_argument("-t", "--threshold", type=int, help="Threshold if thresholding", required=False)
    arg_parser.add_argument("-m", "--method", type=str, help="Threshold/Edge Detection/Smoothing method",
                            required=False)
    arg_parser.add_argument("-k", "--kernel-size", type=int, nargs="+",
                            help="Kernel Size/Shape. Int for edge detection, tuple for smoothing")
    # This is too manual, will have to generalize later
    arg_parser.add_argument("-sm", "--sigma", type=float, help="Sigma for gaussian smoothing", required=False)
    arg_parser.add_argument("-mk", "--mask", type=str, help="Mask if detecting edges", required=False)
    # Switch statement based on target operation
    arguments = arg_parser.parse_args()
    #print(arguments)
    init_call = Segmentation(arguments.directory, image_suffix=arguments.suffix)

    if arguments.operation == "detect_edges":
        sigma = None
        ksize = arguments.kernel_size
        if arguments.mask is not None:
            sigma = arguments.sigma
        if arguments.method in ["sobel_vertical", "sobel_horizontal"]:
            ksize = ksize[0]
        other_plot = init_call.detect_edges(operator=arguments.method,
                                            optional_mask=arguments.mask,
                                            kernel_size=ksize,
                                            sigma=sigma)
    elif arguments.operation == "threshold":
        other_plot = init_call.threshold_images(threshold_method=arguments.method,
                                                use_threshold=arguments.threshold,
                                                use_max=arguments.max_threshold)
    else:
        sigma = None
        if arguments.method == "gaussian":
            sigma = arguments.sigma
        other_plot = init_call.smooth(mask=arguments.method,
                                      kernel_shape=tuple(arguments.kernel_size),
                                      sigma=sigma)

    show_images(init_call.read_images(), other_plot)
    plt.show()
