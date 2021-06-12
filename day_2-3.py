#Mathematical Operations in Python

#Addition Operator
print(3+3)

#Subtraction Operator
print(3-3)

#Multiplication Operator
print(3*3)

#Division operator(Using this will always give the output in float datatype)
print(3/3)

#Exponential Opertor(If you need num1 to the power of num2 then use this)
print(2 ** 2)

#While performing the operations the code will follow the PEMDAS rule from Left to Right
"""PEMDAS 
()
**
* /
+ -
Both (* /) and (+ -) have equal weightage but whichever comes first from left will be calculated first
"""
#The below example will calculate in this order PEMDAS
print(3 * 3 + 3 / 3 - 3)

#The below example will calculate in PEMDAS order but since '/' comes first it will calculate that before '*'
print(3 / 3 + 3 * 3 - 3)

print(3 * (3 + 3) / 3 - 3)
