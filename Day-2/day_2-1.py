#Type Error

#char_count = len(input("What is your name?"))
#print(char_count)
#print("Your name has " + char_count + "characters")

#On Running the above code you will get this error
#Traceback (most recent call last):
#  File "C:\Users\Partha\Desktop\Python_Basics\day_2-1.py", line 4, in <module>
#    print("Your name has " + char_count + "characters")
#TypeError: can only concatenate str (not "int") to str

#The reason is that we cannot concatenate string and integer together


#Type Checking

char_count = len(input("What is your name?"))
print(type(char_count)) #type() checks which datatype does the input belong to


#Type Conversion
char_count = len(input("What is your name?"))
print(char_count)
new_char_count = str(char_count) #Here char_count is converted to string type using str(), we can also convert to float using float()
print(type(new_char_count))
print("Your name has " + new_char_count + "characters")