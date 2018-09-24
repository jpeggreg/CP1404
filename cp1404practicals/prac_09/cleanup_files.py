"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os
import re


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        if ' ' in filename:
            # replace space with underscore
            new_name = get_fixed_filename(filename)

        elif ' ' not in filename:
            # insert underscore between lower and uppercase characters
            temp_name = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', filename)
            new_name = temp_name.replace(" ", "_").replace(".TXT", ".txt")

        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)

        # Option 1: rename file to new name - in place
        #os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


'''def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics/Christmas')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

    for filename in filenames:
        full_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, get_fixed_filename(filename))
        os.rename(full_name, new_name)'''


main()
#demo_walk()