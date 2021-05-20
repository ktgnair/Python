# Functions with Inputs

# Simple Function
def greet():
    print("Hi Goutham")
    print("How are you?")
    print("Is everyone well at home?")

greet()

# Function with Input 
# Here the variable "name" is the parameter and the value "Goutham" is the argument 
def greet_with_name(name):
    print(f"Hi {name}")

greet_with_name("Goutham")

# Function with more than 1 Input
def greet_with(name, location):
    print(f"Hi {name}")
    print(f"How is {location}")

greet_with("Goutham", "Chennai")

# Positional Argument
# In the below value passing statements we are not defining for which parameter we need to pass the particular argument
# So it will take the values based on the position
# i.e. on passing [greet_using_positional_argu("Goutham", "Chennai")] name = Goutham and Location = Chennai
# but on passing [greet_using_positional_argu("Chennai", "Goutham")] name = Chennai and Location = Goutham

def greet_using_positional_argu(name, location):
    print(f"Hi {name}")
    print(f"How is {location}")

greet_using_positional_argu("Goutham", "Chennai")
# greet_using_positional_argu("Chennai", "Goutham")


# Keyword Argument
# In the below value passing statements we are defining for which parameter we need to pass the particular argument
# So it will take the values based on the parameter even if we interchange the position of values
# i.e. on passing [greet_using_positional_argu(name = "Goutham", location = "Chennai")] name = Goutham and Location = Chennai
# and on passing [greet_using_positional_argu(location = "Chennai", name = "Goutham")] name = Goutham and Location = Chennai

def greet_using_positional_argu(name, location):
    print(f"Hi {name}")
    print(f"How is {location}")

# greet_using_positional_argu(name = "Goutham", location = "Chennai")
greet_using_positional_argu(location = "Chennai", name = "Goutham")

