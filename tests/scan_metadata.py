'''
Purpose: Scan through all the metadata files and check what relevant fields there are.
'''
# Standard module import
import os

# Get the default folder
fol = os.getenv('PHOTO_FOLDER')

def main():
    # Verify that we have a folder
    if fol is None:
        raise Exception("ERROR: You must provide a folder by setting the PHOTO_FOLDER env variable!")
    
    # Loop through all the .json files in the folder
    for root, dir, files in os.walk(fol):
        
        # Loop through all the files
        for file in files:

            # Only look at .json files
            if not file.endswith('.json'):
                continue

            # Look at the file contents
            # TODO
            
            # DEBUG: Look at the file path
            # print(os.path.join(root, file)) # TEMP




# Run the main function if this script is called directly
if __name__ == '__main__':
    main()