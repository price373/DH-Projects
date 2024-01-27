import os
# We import sys for the function sys.exit to exit the program at any given point
import sys


def getFileSafely(path):
    if os.access(path, os.R_OK):
        file = open(path)
        return file
    else:
        sys.exit(1)
    '''
    Function to safely open a file object. If `path` can be accessed, open the
      file located at `path` and return it. If `path` does not exist or cannot
      be `access`ed, the program exits by calling `sys.exit(1)` after warning
      the user that `path` is not accessible.
    '''
    pass

if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    file = getFileSafely(filename)
    # The following line should *NEVER* get executed if `filename` is invalid
    file.close()
