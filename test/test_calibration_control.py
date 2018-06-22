from ..tools import calibration_control as cc
import os
import yaml

# Define the test file location
os.chdir('test')
os.chdir('test_files')


def test_import():
    # name the test file
    test_input_file = 'input_example.yaml'
    test_file_data = {'camera_name': 'SC6700', 'integration_time': 1e-4,
                      'temperatures': (100, 200, 300, 400, 500)}
    with open(test_input_file, 'w+') as input_file:
        yaml.dump(test_file_data, input_file)
    camera_settings, temp_profile = cc.read_imput(test_input_file)
    print(camera_settings, temp_profile)
    assert set(temp_profile) == set(test_file_data.pop('temperatures'))
    assert camera_settings == test_file_data


