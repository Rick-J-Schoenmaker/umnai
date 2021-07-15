from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["ACME"]
mycol = mydb["Vehicles"]

mydict = {"Type": "Car", "Make": "Land Rover", "Model": "freelander 2", "Year": 2007, "Seat capacity": 5, "Roof rack availability": True}

x = mycol.insert_one(mydict)

print(mycol.find_one())