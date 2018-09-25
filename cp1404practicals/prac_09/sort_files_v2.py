"""
CP1404 Practical 9
Sort files into directory depending on extension V2
"""

import shutil
import os
from collections import defaultdict


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # create list of all file extensions
    ext_list = []
    filenames = os.listdir('.')
    for filename in filenames:
        ext = filename[filename.find('.'):].strip(".")
        if ext in ext_list:
            pass
        else:
            ext_list.append(ext)
    print(ext_list)

    # create list of category keys to associate with extensions based on user input
    key_list = ['Docs', 'Docs', 'Images', 'Images', 'Docs', 'Spreadsheets', 'Spreadsheets', 'Images']
    '''for ext in ext_list:
        new_key = input("What category would you like to sort {} files into?".format(ext))
        key_list.append(new_key)'''
    print(key_list)

    # merge lists into dictionary grouping file extensions into each category
    temp_dict = defaultdict(list)
    for i, ext in zip(key_list, ext_list):
        temp_dict[i].append(ext)
    ext_dict = dict(temp_dict)
    print(ext_dict)

    for key in ext_dict:
        try:
            os.mkdir(key)
            for i, value in ext_dict.values():
                if filename[filename.find('.'):].strip(".") == (value[i]):
                       shutil.move(filename, key)
        except:
            FileExistsError
            print("Folder already exists")


    # Loop through each file in the (current) directory to ask user for file group category
    #for filename in os.listdir('.'):
     #   ext_name = filename[filename.find('.'):]
      #  ext_dict[""] = input("What category would you like to sort {} files into?".format(ext_name))



main()