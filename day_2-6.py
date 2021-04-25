#Your Life in Weeks
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

current_age = int(input("What is your current age\n"))

expectency_age = int(input("Type the life expectency\n"))

years_remaining = expectency_age - current_age

days_left = years_remaining * 365
months_left = years_remaining * 12
weeks_left = years_remaining * 52

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
