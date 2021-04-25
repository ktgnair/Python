# Using For Loop with Python lists.
fruits = ["Apple", "Mango", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Using For Loop with Range.
# Range prints the value or takes the range till n-1 i.e range(1,10) will print till 9
for number in range(1, 10):
    print(number)

# # Say we need to print till 10 the keep the range 1 number ahead.
for number in range(1, 11):
    print(number)

# If we need to print with a step of 2 then do the below.
for number in range(1, 10, 2):
    print(number)

# Using range addition of numbers from 1-100
total = 0
for numbers in range(1, 101):
    total += numbers
print(total)