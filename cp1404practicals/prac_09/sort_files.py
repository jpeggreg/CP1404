"""
CP1404 Practical 9
Sort files into directory depending on extension
"""

import shutil
import os

def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

    # create list of all file extensions
    ext_names = []
    names = os.listdir('.')
    for name in names:
        new_name = name[name.find('.'):]
        ext_names.append(new_name)
    print(ext_names)

    # create folders named after each file extension with error exception
    for ext in ext_names:
        try:
            os.mkdir(ext)
            # move specific file to new folder based on extension
            for filename in os.listdir('.'):
                if filename[filename.find('.'):] == ext:
                    shutil.move(filename, ext)
        except:
            FileExistsError
            print("Folder already exists")
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

main()
