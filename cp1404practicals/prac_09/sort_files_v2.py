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

    # create list of category keys to associate with extensions based on user preference
    # test functionality without needing user input: key_list = ['Docs', 'Docs', 'Images', 'Images', 'Docs', 'Spreadsheets', 'Spreadsheets', 'Images']
    key_list = []
    for ext in ext_list:
        new_key = input("What category would you like to sort {} files into?".format(ext))
        key_list.append(new_key)
    print(key_list)

    # merge lists into dictionary grouping file extensions with chosen category
    ext_dict = defaultdict(list)
    for i, ext in zip(key_list, ext_list):
        ext_dict[i].append(ext)

    # make each directory from key_list based on user input
    for key in ext_dict:
        try:
            os.mkdir(key)
        except:
            FileExistsError
            print("Folder already exists")

    # move each file to a directory based on input by user (ext_list)
    for filename in os.listdir('.'):
        for value in ext_dict.values():
            if filename[filename.find('.'):].strip(".") in value:
                key = list(ext_dict.keys())[list(ext_dict.values()).index(value)]
                shutil.move(filename, key)


main()