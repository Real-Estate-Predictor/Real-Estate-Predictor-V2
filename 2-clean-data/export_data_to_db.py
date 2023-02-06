import csv
import pymongo

fpath = './data/afterCleaning.csv'

try:
    mongo = pymongo.MongoClient(
        host='localhost', 
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.company
    collection = db['houseData']
    header = [
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
        'depth'
    ]
    csvFile = open(fpath, 'r')
    render = csv.DictReader(csvFile)

    for each in render:
        row = {}
        for field in header:
            row[field] = each[field]
        print(row)
        collection.insert(row)
    mongo.server_info() # trigger exception if cannot connect to db
except Exception as e:
    print(e)
    print('ERROR - Cannot connect to db')
