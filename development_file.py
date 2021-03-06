"""
This file is used to test the functionality of the modules and functions under development and to help
with creating tests.
"""
from tools import black_body_interface as bbi
from tools import sfmov_converter as sc
from tools import image_analysis as ia
import os
import numpy as np
from skimage.viewer import ImageViewer



if __name__ == '__main__':
    sfmov_path = os.path.join(os.path.abspath('.'), 'test/test_files/')
    file_name = "ir_test_file"
    # se = sc.SfmovTools(sfmov_path, sfmov_path, file_name)
    # print(se.camera_name)
    # se.convert(compression_factor=0)
    test_image = ia.Image_Tools(sfmov_path, file_name)
    # data = test_image.read_frames('0:2')
    # test_image.show_image('0:2')
    test_image.crop_from_roi()


