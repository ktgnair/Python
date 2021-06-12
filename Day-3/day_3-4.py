# Leap Year
# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.

current_year = int(input("Please enter a year of your choice: "))

if current_year % 4 == 0:
    if current_year % 100 == 0:
        if current_year % 400 == 0:
            print("Its a Leap Year")
        else:
            print("Its not a Leap Year")   
    else:
        print("Its a Leap Year") 
else:
    print("Its not a Leap Year")


