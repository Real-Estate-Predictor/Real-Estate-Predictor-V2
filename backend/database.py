import pymongo
try:
    mongo = pymongo.MongoClient(
        host='localhost', 
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    mongo.server_info() # trigger exception if cannot connect to db
    db = mongo.company
except:
    print('ERROR - Cannot connect to db')