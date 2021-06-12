#Tip Calculator
#If the bill is 150.00, split between 5 people, with 12% tip. 
#Each person should pay 33.6
#Output the result to 2 decimal places

print("Welcome to the Tip Calculator.")

bill_amount = float(input("What is the Total bill?  Rs"))
tip_percent = int(input("What percent of tip would you like to give? "))

tip_amount = (bill_amount * tip_percent) / 100
total_amount_to_pay = bill_amount + tip_amount 

no_of_people = int(input("With how many people you need to split the bill amount? "))
split_amount = round(total_amount_to_pay / no_of_people, 2)
#Here on using round() the output will not give 2 decimals if the round off is till 1 digit
#Example : 33.6 but we want 33.60, so for that we can use the below formatting way
split_amount = "{:.2f}".format(total_amount_to_pay / no_of_people)#Here the output of the calculation gives float but its converted to string and giving output using the formatting rules

print(f"Each person should pay: Rs{split_amount}")