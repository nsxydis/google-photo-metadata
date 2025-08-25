'''
Purpose: Test merging metadata into a photo.
'''
# Standard modules
import os
import json
import exif

# Default folders
input_folder = os.getenv('TEST_INPUT')
output_folder = os.getenv('TEST_OUTPUT')

# TEMP
print(input_folder)

# Exepected image types
expected = [
    '.jpg',
    '.jpeg',
    '.png',
]

def test_add_data():
    '''Test adding metadata to a file and moving it to the output folder'''
    # Loop through all the files in the test folder
    for root, dirs, files in os.walk(input_folder):

        # Loop through each file in the input folder
        for file in files:

            # Only look at expected image types
            for item in expected:

                # Break if we found one that we're looking for
                if file.endswith(item):
                    
                    # Make the name of the metadata file we'd expect
                    metadata_file_name = file.strip(item) + '.j.json'
                    break

            # Otherwise, we didn't find an expected file type and should skip
            else:
                continue

            # Check that we have a metadata file in our files
            if metadata_file_name not in files:
                continue

            # Get the file paths
            path = os.path.join(root, file)
            meta_path = os.path.join(root, metadata_file_name)
            out_path = os.path.join(output_folder, file)

            # Open the image file
            with open(path, mode = 'rb') as image_file:
                
                # Read in the image
                image = exif.Image(image_file)

            # Open the metadata file
            with open(meta_path, mode = 'r') as f:
                
                # Read the metadata
                metadata = json.load(f)

            # Add the metadata to the image file
            image = recursive_set(image, metadata)

            # Write the Date Taken
            image.set(
                "Date Taken",
                metadata['photoTakenTime']['timestamp']
            )

            # Output the image file
            with open(out_path, 'wb') as f:
                f.write(image.get_file())

# XXX: Obsolete
def recursive_set(image: exif.Image, metadata: dict) -> exif.Image:
    '''Recursively set the metadata'''
    for key, value in metadata.items():
        if type(value) is not dict:
            image.set(key, value)
        else:
            image = recursive_set(image, value)

    return image

