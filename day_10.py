# Functions with Outputs.

# In a normal function if we do the below then we will get an error as result is not defined
# def new_function():
#     result = 3*2
# new_function()
# print(result)

# But using 'return' keyword in the below code we are able to store the output of a function i.e Functions with Outputs
def my_function():
    result = 3 * 2
    return result

output = my_function()
print(output)

# String title()
# The title() function in python is used to convert the first character in each word to Uppercase and remaining characters to Lowercase in the string and returns a new string.
def format(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

name = format("kt","GOUtHAM")
print(name)
# Alternative way print(format("kt","GOUtHAM"))

# Multiple return values
# 'return' keyword tells the computer that the function is over and need to move further
# eg: The below code

# def format(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "The input is invalid"

#     first_name = f_name.title()
#     last_name = l_name.title()
#     return f"{first_name} {last_name}"

# name = format(input("Enter the first name"), input("Enter the last name"))
# print(name)

# The above code will stop if the input is empty and will not run beyond the if statement.