def replace_spaces_and_lower(s):
    # Replace blank spaces with hyphens and convert the string to lowercase
    result = s.replace(" ", "-").lower()
    return result

def process_string_list(string_list):
    # Apply the replace_spaces_and_lower function to all strings in the input list
    return [replace_spaces_and_lower(s) for s in string_list]


# create file if not exists
def create_file_if_not_exists(path):
    try:
        # Open the file in "x" mode, which creates a new file and raises an exception if it already exists
        with open(path, "x") as file:
            pass  # Do nothing, just create the file
    except FileExistsError:
        pass