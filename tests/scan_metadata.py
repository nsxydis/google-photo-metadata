'''
Purpose: Scan through all the metadata files and check what relevant fields there are.
'''
# Standard module import
import os
import json

# Get the default folder
fol = os.getenv('PHOTO_FOLDER')

def main():
    # Verify that we have a folder
    if fol is None:
        raise Exception("ERROR: You must provide a folder by setting the PHOTO_FOLDER env variable!")
    
    # Init a dictionary
    key_count = {}
    
    # Loop through all the .json files in the folder
    for root, dirs, files in os.walk(fol):
        
        # Loop through all the files
        for file in files:

            # Only look at .json files
            if not file.endswith('.json'):
                continue

            # Get the file path
            path = os.path.join(root, file)

            # Look at the file contents
            with open(path, mode = 'r', encoding = 'utf-8') as f:
                # Read in the json data
                data = json.load(f)

                # Increment our key counter
                for item in data.keys():
                    try:
                        key_count[item] += 1
                    except:
                        key_count[item] = 1

    # Print out the final results
    for key, value in key_count.items():
        print(f'{key}: {value}')

    # NOTE: I found a couple of files with geoDataExif -- these don't seem to contain unique information and can be ignored


# Run the main function if this script is called directly
if __name__ == '__main__':
    main()