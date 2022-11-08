import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["elephantDetection"]
mycol = mydb["elephant"]

def insertOne(dataDict):
    print("The database exists.")
    # mydict = { "name": "John", "address": "Highway 37" }
    mycol.insert_one(dataDict)

# dblist = myclient.list_database_names()
# if "elephantDetection" in dblist:
#   print("The database exists.")


# collist = mydb.list_collection_names()
# if "elephant" in collist:
#   print("The collection exists.")