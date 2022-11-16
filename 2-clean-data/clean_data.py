"""
This script is used to clean data from step 1.

usage:
python3 clean_data.py path_to_filename.csv path_to_outfile.csv
"""

from sys import argv

def main():
    """
    cleans data from input
    """

    filepath = argv[1]
    outfilepath = argv[2]
    
    print("Cleaning data...")


if __name__ == "__main__":
    main()
