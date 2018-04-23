"""
Interface with an Electro Optical Industries Blackbody Radiation Source
Temperature Controller Model 2500E/R

author: Derek Bean
"""
import os
import subprocess


class BlackBody_Control():
    """Control and interface with the blackbody temperature controller over
       a RS232 connection using c programs written and compiled with python
       will be editing this in the future using cython and other tools that
       will be better in the future
    """
    def __init__(self):
        self.directory = os.path.dirname(os.path.abspath(__file__))
        return

    def write_file(self, input_text, filename='control_file.c'):
        """Generate a c file that can be used to communicate with the blackbody
        in the desired way. The initial text file is just a hello world C
         script that is imported with future options to recive text input from
         the command line among other options
        """
        filepath_string = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            filename)
        with open(filepath_string, 'w+') as control_file:
            [control_file.write(x) for x in input_text]
        return filepath_string

    def compile_file(self, c_name):
        """ Compile the C file to create a an executatble c file. Eventually
        this will work for both Windows and Linux but it will initially be
        linux only"""
        subprocess.run('gcc -o {0} {1}'.format([c_name, file_name]))
        return

    def run_program(self):
        """Execute the previously compiled program for the communication
        protocol
        """
        test= 0
        return
