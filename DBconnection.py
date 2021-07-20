from pymongo import MongoClient
from bson.objectid import ObjectId
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["ACME"]
mycol = mydb["Vehicles"]

# Define search_value(key, value) function can be called to search for a value in the database.
def search_value(key, value):
    temp = mycol.find({key: {"$regex": value}})
    result = []
    for res in temp:
        result.append(res)
    if len(result) >= 1:
        return result

# Define search_vin(key, value) function can be called to search for a specific VIN (id) in the database.
def search_vin(key, value):
    result = mycol.find_one({key: value})
    return result

# Define getall(key) function can be called to get all values from the database matching a specific key.
def getall(key):
    temp = mycol.distinct(key)
    result = []
    for res in temp:
        result.append(res)
    if len(result) >= 1:
        return result

# Define insert_db(key) function can be called to insert a single vehicle to the database.
def insert_db(key):
    temp_dict = key
    mycol.insert_one(temp_dict)
    result = "Update was succesfull"
    return result

# Define delete_from_db(key) function can be called to delete a single vehicle from the database
def delete_from_db(key):
    id = key
    print(id)
    mycol.delete_one({'_id': id})
    result = "Delete of vehicle was succesfull"
    return result
