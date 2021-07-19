from pymongo import MongoClient
def createandfill():
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["ACME"]
    mycol = mydb["Vehicles"]

    mydict = {"_id": 1, "Type": "Car", "Make": "Land Rover", "Model": "Freelander 2", "Year": 2007, "Seat capacity": 5,
          "Roof rack availability": True}, {"_id": 2, "Type": "Truck", "Make": "Scania", "Model": "XL",
                                            "Year": 2013, "Haul capacity": 1000},\
        {"_id": 3, "Type": "Motorcycle", "Make": "Harley Davidson", "Model": "XL", "Year": 2011,
          "Sidecar capacity": True}, {"_id": 4, "Type": "Car", "Make": "Land Rover", "Model": "Defender", "Year": 1999, "Seat capacity": 5,
          "Roof rack availability": True}, {"_id": 5, "Type": "Truck", "Make": "DAF", "Model": "XL2000",
                                            "Year": 2017, "Haul capacity": 2000},\
        {"_id": 6, "Type": "Motorcycle", "Make": "Kawasaki", "Model": "Ninja", "Year": 2015,
          "Sidecar capacity": False}

    x = mycol.insert_many(mydict)
    # x = mycol.delete_many({})
    for x in mycol.find():
        print(x)

createandfill()