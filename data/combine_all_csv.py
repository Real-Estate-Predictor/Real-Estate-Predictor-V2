import os
import glob

# create file if not exists
def create_file_if_not_exists(path):
    try:
        # Open the file in "x" mode, which creates a new file and raises an exception if it already exists
        with open(path, "x") as file:
            pass  # Do nothing, just create the file
    except FileExistsError:
        pass

# Set the directory containing the TXT files
txt_directory = "./raw_2023_04_19"

# Set the directory containing the TXT files
output_directory = "./raw_2023_04_19"

# Create a new output file with a unique name
output_file_name = "combined_output.csv"

output_file_path = os.path.join(output_directory, output_file_name)

# Create the output directory if it does not exist
os.makedirs(output_directory, exist_ok=True)

# Find all TXT files in the directory
txt_files = glob.glob(os.path.join(txt_directory, "*.csv"))

create_file_if_not_exists(output_file_path)

# Open the output file
with open(output_file_path, "w") as outfile:
    # Read and append each TXT file
    for txt_file in txt_files:
        with open(txt_file, "r") as infile:
            # Read the contents of the file
            content = infile.read()
            # Append the content to the output file
            outfile.write(content)
            # Optionally, add a newline character to separate the content of different files
            # outfile.write("\n")
