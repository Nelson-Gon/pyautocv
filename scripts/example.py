
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from .. import simplecv


images_list = list(read_images("../images"))
thresheld = threshold(images_list)
thresheld_converted = convert_thresheld(thresheld, images_list)
edge_detection = list(map(lambda x: detect_edges("laplace",x), thresheld_converted))
show_images(convert_thresheld(thresheld_list, images_list),thresheld=True,ncols=2)
show_images(edge_detection, ncols=2, thresheld=True)