# Prime Number Checker
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4

user_input = int(input("Enter the number of your choice "))
def prime_checker(number):
    count = 0
    for n in range(1,number+1):
        if(number % n == 0):
            count += 1
            print(count)

    if(count == 2): # The count should be 2 because a number is prime if its divisible either by 1 or by the number itself. So only 2 time that condition occurs.
        print(count)
        print("It's a prime number")
    else:
        print("It's not a prime number")

prime_checker(number=user_input)

# Alternative Way
# def prime_checker(number):
#     is_Prime = True
#     for n in range(2,number):
#         if(number % n == 0):
#             is_Prime = False
#     if is_Prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
