# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python script for conducting image analysis on infrared images
@author: Derek Bean
"""

import os
import tables as tb
import skimage as si
from skimage.viewer import ImageViewer
import numpy as np
import skimage.io as io

class Image_Tools():
    def __init__(self, file_path, file_name):
        self.file_path = self.path_handling(file_path)
        self.file_name = file_name
        self.data_attributes = {}

    @staticmethod
    def path_handling(path):
        """ TODO: Need to remove and replace function with os package for path handling across operating systems"""
        path.replace('\\', '/')
        if path[0] == '/':
            path = '/' + path
        return path


    def open_hdf5(self):
        """
        Open and return a file object based on the input path

        Input:
        extension: a string with the
        """
        return tb.open_file(os.path.join(self.file_path, self.file_name + '.hdf5'), 'r')

    def get_attributes(self):
        """
        Get the values for important parameters from the hdf5 file such as dropped frames and the frame rate

        :returns a dictionary of the important attributes with the keys the same as those in the hdf5 file
        """
        data = {}
        with self.open_hdf5() as file:
            for dataset in file.root:
                if 'data' not in dataset.name:
                    data[dataset.name] = dataset.read()
        self.data_attributes = data
        return self.data_attributes

    def read_frames(self, frame_number=-1):
        """

        :param frame_number: desired frames to pull in. defaults to all frames (-1). Can use slice like notation
                             in a string format ie frame_number='0:2' returns the first and second frame
        :return: returns a numpy ndarray of the data
        """
        try:  # Check to see if the file info has been loaded if not load the file data
            self.data_attributes['number_of_frames']
        except KeyError:
            self.get_attributes()
            self.read_frames(self, frame_number)
        with self.open_hdf5() as file:  # Ra=ead the frames from the hdf5 file based on the frame number input
            if frame_number == -1:  # Read all of the frames
                frame_dataset = file.root.data.read()
            else:
                # Handle the string notation format of the frame slices to get the start and stop points
                if type(frame_number) == str:
                    start = int(frame_number.split(':')[0])
                    stop = int(frame_number.split(':')[-1])
                elif type(frame_number) == int:
                    start = frame_number
                    stop = frame_number + 1
                frame_dataset = file.root.data.read(start, stop)

        return frame_dataset

    def show_image(self, frame_number):
        """
        Display desired images from the file in a popup window. Can display multiple images in sequence

        Input:
            frame_number: desired frame number to show. can also use slice like notation encapsulated in a string
                            for example frames 0 and 1 could both be displayed with the input '0:2'. Also accepts ints
        """
        image = self.read_frames(frame_number)
        for frame in range(np.shape(image)[0]):
            viewer = ImageViewer(image[frame,:,:])
            viewer.show()


    def img_rms(self):
        return None

    def define_roi(self):
        return None

    def background_subratction(self):
        return None