#BMI Calculator
#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height and convert the result to a whole number..
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

height = float(input("Enter your height in m\n"))
weight = float(input("Enter your weight in kg\n"))

bmi = weight / (height ** 2)
bmi_in_int = int(bmi)

print("Your BMI is " + str(bmi_in_int))

