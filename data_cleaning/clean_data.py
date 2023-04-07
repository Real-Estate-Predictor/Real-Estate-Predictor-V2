"""
Usage:

python3 clean_data.py ./data/raw_data.csv ./data/clean_housing_data.csv
"""
import pandas as pd
import datetime
import warnings
from sys import argv
warnings.filterwarnings('ignore')


def clean_data(file_path, out_file_path):

    data = pd.read_csv(file_path, header=None, on_bad_lines='skip')

    data.columns = column_names = [
    "address",
    "price",
    "gross_tax",
    "strata_maintenance_fees",
    "bedrooms",
    "bathrooms",
    "property_type",
    "property_age",
    "title",
    "style",
    "heating_type",
    "feature",
    "amenities",
    "appliances",
    "community",
    "days_on_rew",
    "property_views",
    "mls®_number",
    "source",
    'frontage', 
    'lot_size', 
    'year_built', 
    'depth']



    # Filter Houses Only
    houses = data[data['property_type'] == 'house']

    # Convert Price column to integer
    houses["price"] = houses["price"].str.replace(",", "").str.replace("$", "")
    houses["price"] = pd.to_numeric(houses["price"])

    # extract the lot width from the lot_size column
    houses["lot_width"] = houses["lot_size"].str.extract(r"^(\d+) ft x")

    # extract the lot length from the lot_size column
    houses["lot_length"] = houses["lot_size"].str.extract(r"(\d+) ft x")

    # extract the lot size from the lot_size column
    houses["lot_size"] = houses["lot_size"].str.extract(r"\((\d+) ft²\)")


    # Convert Gross Tax Income to Integer
    houses['gross_tax'] = houses['gross_tax'].astype(str)
    houses['gross_tax'] = houses['gross_tax'].str.replace(',', '')
    houses['gross_tax'] = houses['gross_tax'].str.replace('$', '')
    houses['gross_tax'] = houses['gross_tax'].astype(int)

    # Convert House Age to integer - Consider prebuild houses with age 0
    # extract the year from the year_built column
    houses["year_built"] = houses["year_built"].str.extract(r"(\d+)")

    # compute the age of the house using the current year
    current_year = datetime.datetime.now().year
    houses["age"] = current_year - pd.to_numeric(houses["year_built"])

    ## remove duplicate based on mls number
    houses = houses.drop_duplicates(subset=['mls®_number'])

    houses = houses.drop(['property_age','strata_maintenance_fees', 'property_views'], axis=1)

    # extract bungalow information
    houses["bungalow"] = houses["style"].str.contains("bungalow").fillna(-1).astype(int)

    # extract storey information
    houses["storey"] = houses["style"].str.extract(r"(\d+)").fillna(-1).astype(int)

    # extract basement information
    houses["basement"] = houses["style"].str.contains(" w/bsmt").fillna(-1).astype(int)

    # extract laneway house information
    houses["laneway_house"] = houses["style"].str.contains("laneway house").fillna(-1).astype(int)

    # Extract garage house information:
    houses["garage"] = houses["feature"].str.contains("garage").fillna(-1).astype(int)


    # extract split entry information
    houses["split_entry"] = houses["style"].str.contains("split entry").fillna(-1).astype(int)
    houses = houses.drop(['style'], axis=1)

    # these columns can be cleaned more thoroughly, but they are not as important at the moment
    houses = houses.drop(['title','amenities','heating_type', 'days_on_rew', 'appliances', 'feature', 'source', 'frontage', 'mls®_number','depth'], axis=1)


    # IMPORTANT:
    """
    We need to get the GEO Cordinates for address. We will drop the column for now
    """

    # houses = houses.drop(['address'], axis=1)

    
    # write to file
    houses.to_csv(out_file_path)


if __name__ == "__main__":
    """
    cleans data from input
    """
    filepath = argv[1]
    outfilepath = argv[2]

    clean_data(file_path=filepath, out_file_path=outfilepath)