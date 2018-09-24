"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
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
            # replace any space with underscore
            new_name = get_fixed_filename(filename)

        elif ' ' not in filename:
            # insert underscore between any lower and uppercase characters
            temp_name = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', filename)
            new_name = temp_name.replace(" ", "_").replace(".TXT", ".txt")

        print("Renaming {} to {}".format(filename, new_name))
        # rename each file as per above prerequisites
        os.rename(filename, new_name)

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename if it contains space or uppercase extension."""
    if ' ' in filename or ".TXT" in filename:
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    else:
        new_name = filename
    return new_name


main()
#demo_walk()