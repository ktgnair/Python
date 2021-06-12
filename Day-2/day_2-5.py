#Number Manipulation and F-Strings

print(8 / 3)

#In the above example we get the output as 2.6666666666666665 but say we need to round off the number then use round()
print(round(8 / 3))

#Rounding off the number upto 2 decimals round(number to be rounded off, number of decimals to be rounded off)
print(round(8 / 3, 2))

#As the output of division is floating datatype we can use flow division(//) for integer datatype.
#The // will print the output before the decimal and in integer datatype
print(8 // 3)

#Short-hand way of using mathematical operators
result = 2
result += 2 #This is similar to result = result + 2
print(result)

#For printing different datatypes together we need to convert it to string like below
num1 = 10
num2 = 2.4
print("Your first number is " + str(num1) + ", Your second number is " + str(num2))#But here its difficult to convert everything

#F strings
#Since its difficult to convert every variable  while printing we can use F strings to print the value as it is without any type conversion
print(f"Your first number is {num1}, Your second number is {num2}")


