from ..tools import calibration_control as cc
import os

# Define the test files
os.chdir('test')
os.chdir('test_files')
test_input_file = 'input_example.yaml'


def test_import(test_input_file):
    camera_settings, temp_profile = cc.read_imput(test_input_file)
    print(camera_settings, temp_profile)