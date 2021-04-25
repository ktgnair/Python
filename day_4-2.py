# Lists in Python
# List is a type of Data Structue in python.
# Multiple functions are available in list. Please refer the google for different thing that can be done in lists.

# List can have multiple values of different datatypes inside it.
# We can access the list elements using index value.
colour_available = ["Blue", "Green", "Red", "Yellow", "Orange", "Violet", "Purple", 1]
print(colour_available[7])

# We can also access the list elements from end to start using negative indexing.
print(colour_available[-1])

# We can modify the values of list
colour_available[0] = "Blu"
print(colour_available)

# We can add a new value in list. 
# Since the list maintains the order so the value will be added at the end of the list.
colour_available.append("Black")
print(colour_available)

# We can add multiple values in list.
colour_available.extend(["Grey", "White"])
print(colour_available)

# Nested Lists
fruits = ["Apple", "Mango", "Pear", "Orange"]
vegetables = ["Potato", "Brinjal", "Carrot", "Radish"]

food_items = [fruits, vegetables] # This is an example of Nested lists
print(food_items)
print(food_items[0]) #Output will be fruits list
# If we want any one item inside the fruits list
print(food_items[0][1])# This will print the value at index position 1 inside the fruits list




