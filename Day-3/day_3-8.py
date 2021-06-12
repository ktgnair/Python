# Love Calculator
# Write a program that tests the compatibility between two people.
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

print("Cupid's Calculator!!")

name_of_person1 = input("Enter your name \n")
name_of_person2 = input("Enter your partners name \n")

combined_names = name_of_person1 + name_of_person2
person_name_in_lower = combined_names.lower()

true_total = person_name_in_lower.count('t') + person_name_in_lower.count('r') + person_name_in_lower.count('u') + person_name_in_lower.count('e')
love_total = person_name_in_lower.count('l') + person_name_in_lower.count('o') + person_name_in_lower.count('v') + person_name_in_lower.count('e')
loveScore = int(str(true_total) + str(love_total))

if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")