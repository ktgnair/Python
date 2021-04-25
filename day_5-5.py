# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator Program ")
total_letters = int(input("How many letters would you like in your Password?\n"))
total_numbers = int(input("How many numbers would you like in your Password?\n"))
total_symbols = int(input("How many symbols would you like in your Password?\n"))

password1 = random.sample(letters,total_letters) #Will return a random sample of the mentioned length - total_letters 
password2 = random.sample(numbers,total_numbers)
password3 = random.sample(symbols,total_symbols)

final_password = password1 + password2 + password3 #By doing this we will get the password but it will of fixed order letters + numbers + symbols
final_password_new = random.sample(final_password, len(final_password)) #By doing this step we are again finding the random list out of the above  final_password(means it will give output in unknow format, which will make the password tough to crack)

final_password_string = "" #Empty string to concatenate the string inside the for loop
for i in final_password_new:
    # Take one value from the list and concatenate it in the empty string, and finally we will have the whole list in one single string.
    final_password_string += i
print(f"Your Password is: {final_password_string}")