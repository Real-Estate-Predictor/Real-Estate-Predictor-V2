import csv

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception occurred: {e}")
            # If you wish to re-raise the exception after handling, uncomment the following line
            raise
    return wrapper

def write_to_csv(data_dict, column_names, csv_file_path):
    # Create or open the CSV file
    with open(csv_file_path, 'a', newline='') as csv_file:
        # Create a CSV writer
        writer = csv.DictWriter(csv_file, fieldnames=column_names)

        # Write the header if the file is new (i.e., its current size is 0)
        if csv_file.tell() == 0:
            writer.writeheader()

        # Create a new dictionary with the same keys as column_names
        # If the key does not exist in data_dict, it will be set to ""
        row_dict = {col: data_dict.get(col, "") for col in column_names}

        # Write the data to the CSV file
        writer.writerow(row_dict)