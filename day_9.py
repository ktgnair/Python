# The Python Dictionary
# dictionary = {"Key": "Value"} pair

vehicle = {
    "Car": "A vehicle with 4 wheels and a motor",
    "MotorBike": "A vehicle with 2 wheels and a motor",
    "Cycle": "A vehicle with 2 wheels but without motors",
}

# Retrieve the items from a Dictionary
print(vehicle["Cycle"])

# Adding new items to a Dictionary
vehicle["Truck"] = "A large vehicle with 4 wheels and motor"
print(vehicle)

# Creating empty Dictionary
dictionary = {}

# Wipe an existing Dictionary
# vehicle = {}

# Edit an item in the Dictionary
vehicle["Cycle"] = "A common mode of transport"
print(vehicle)

# Loop through a Dictionary
for key in vehicle:
    print(key) #This will give you the key inside the Dictionary
    print(vehicle[key]) #This will give you the values for the particular key inside the Dictionary

