'''
Purpose: Test merging metadata into a photo.
'''
# Standard modules
import os
import exif

# Default folders
input_folder = os.getenv('TEST_INPUT')
output_folder = os.getenv('TEST_OUTPUT')

def test_add_data():
    '''Test adding metadata to a file and moving it to the output folder'''
    # Loop through all the files in the test folder
    for root, dirs, files in os.walk(input_folder):

        # Loop through each file
        for file in files:
            pass