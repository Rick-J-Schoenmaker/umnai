import requests
BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "vin/1", {"Type": "Car", "Make": "Land Rover", "Model": "freelander 2", "Year": 2007, "Seat capacity": 5, "Roof rack availability": True})
print(response.json())
input()
response = requests.get(BASE + "vin/1")
print(response.json())