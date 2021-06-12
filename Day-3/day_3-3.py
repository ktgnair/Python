# BMI Calculator 2.0
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
"""
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""
#Should round the result to the nearest whole number. 

print("Please check your Body Mass Index!")

height = float(input("Please enter the height in m: "))
weight = float(input("Please enter your weight in kg: "))

bmi_value = round(weight / (height ** 2))

print(bmi_value)

if bmi_value < 18.5:
    print("You are Underweight")
elif bmi_value < 25:
    print("You are Normal")
elif bmi_value < 30:
    print("You are Slightly overweight")
elif bmi_value < 35:
    print("You are Obese")             
else:
    print("You are Clinically Obese")