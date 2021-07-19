from pymongo import MongoClient
from bson.objectid import ObjectId
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["ACME"]
mycol = mydb["Vehicles"]
def search_value(key, value):
    temp = mycol.find({key: {"$regex": value}})
    result = []
    for res in temp:
        result.append(res)
    return result

def search_vin(key, value):
    result = mycol.find_one({key: value})
    return result

def getall(key):
    temp = mycol.distinct(key)
    result = []
    for res in temp:
        result.append(res)
    return result


def insert_db(key):
    temp_dict = key
    mycol.insert_one(temp_dict)
    result = "Update was succesfull"
    return result

def delete_from_db(key):
    id = key
    print(id)
    mycol.delete_one({'_id': id})
    result = "Delete of vehicle was succesfull"
    return result
