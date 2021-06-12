#Write a program to build an automatic pizza order program.Based on a user's order, work out their final bill.
"""
Small Pizza: Rs 150
Medium Pizza: Rs 220
Large Pizza: Rs 250
Pepperoni for Small Pizza: +Rs 30
Pepperoni for Medium or Large Pizza: +Rs40
Extra cheese for any size pizza: +Rs 30
"""
print("Welcome to Famous Pizza Plaza")
pizza_size = input("Which pizza would you like to have - S,M or L: \n")
add_pepperoni = input("Do you want to add pepperoni over your pizza. If Yes then enter Y else N: \n")
extra_cheese = input("Do you require extra topping of cheese. If Yes presss Y else N: \n")

pizza_amount = 0

if pizza_size == 'S':
    pizza_amount += 150
elif pizza_size == 'M':
    pizza_amount += 220
else:
    pizza_amount += 250

if add_pepperoni == 'Y':
    if pizza_size == 'S':
        pizza_amount += 30
    else:
        pizza_amount += 40

if extra_cheese == 'Y':
    pizza_amount += 30

print(f"Your final bill is RS {pizza_amount}")