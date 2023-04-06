"""
This script is used to clean data from step 1.

usage:
python3 clean_data.py path_to_filename.csv path_to_outfile.csv YOUR_API_KEY
"""

from sys import argv
import pandas as pd
import requests
def get_latlng(address, api_key):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': api_key}
    response = requests.get(url, params=params).json()
    results = response['results']
    if len(results) > 0:
        location = results[0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None


def main():
    """
    cleans data from input
    """
    filepath = argv[1]
    outfilepath = argv[2]
    # AIzaSyBYEgXeAYKMj4oMSvXOK6yGxpXhQlMArbA
    google_api_key = argv[3]

    # ./data/raw_data.csv
    data = pd.read_csv(filepath, on_bad_lines='skip')

    print(data.head())
    data['latitude'], data['longitude'] = zip(*data['address'].apply(lambda x: get_latlng(x, google_api_key)))

    print("Cleaning data...")
    # data/clean_housing_data.csv
    data.to_csv(outfilepath)


if __name__ == "__main__":
    main()
