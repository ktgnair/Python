# Write a program that adds the digits in a 2 digit number. 
#e.g. if the input was 35, then the output should be 3 + 5 = 8


input_num = input("Enter any two digit number of your choice? \n")

num1 = input_num[0] #Using Subscripting method input_num[0]
num2 = input_num[1] #Using Subscripting method input_num[1]
result = int(num1) + int(num2) #Using Type Conversion as num1 and num2 are of String datatype

#As num1 and num2 are of string datatype so no conversion is needed.
#But result is of Integer datatype, so it needs to converted as we cannot print string and integer together. 
print("The output is " + num1 + " + " + num2 + " = " + str(result))
