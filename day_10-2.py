# Calculator

import calculator_ASCII_art

# Add Function
def add(num1, num2):
    return num1 + num2

# Subtract Function
def subtract(num1, num2):
    return num1 - num2

# Multiply Function
def multiply(num1, num2):
    return num1 * num2

# Divide Function
def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculation():
    print(calculator_ASCII_art.logo)

    first_num = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)

    flag = True
    while flag:
        operator = input("Enter anyone of the operators to perform the calculation: ")
        second_num = float(input("Enter the next number: "))
        operator_function = operations[operator]
        answer = operator_function(first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {answer}")
        
        new_calculation = input(f"Enter 'y' to continue the calculation with {answer} or enter 'n' to start a new calculation: ").lower()
        if new_calculation == "y":
            first_num = answer
        else:
            flag == False
            print("\n" * 100)
            calculation()

calculation()
