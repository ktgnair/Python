#Using nested if statements and elif statements

print("Welcome to the Roller Coster Ride!")

age = int(input("Enter your current age: "))
height = float(input("Please tell you height in cm: "))

if height >= 120:
    print("You are eligible for the ride!")
    if age < 12:
        print("Please pay a fee of 20Rs")
    elif age <=18:
        print("Please pay a fee of 30Rs")
    else:
        print("Please pay a fee of 40Rs")
else:
    print("Sorry! You are not eligible for the ride")
