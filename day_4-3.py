# Banker Roulette - Who will pay the bill? 
# Write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# No usage of choice()

import random

person_names = input("Enter the names of the people who had food with a comma and space - eg: Ram, Shyam\n")

#This will split the names and give the output in form of a list.
person_names_split = person_names.split(", ") 

# Since we need to print the name with respective to index value as list gives output based on index.
pay_bill = random.randint(0, len(person_names_split)-1)

print(f"{person_names_split[pay_bill]} is going to pay the bill!!" )

