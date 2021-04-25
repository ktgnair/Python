# Adding Even Numbers
# Write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# There should only be 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation.

# Method 1
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# Method 2
even_sum = 0
for number in range(2, 101, 2):
    even_sum += number
print(even_sum) #This will print the range with step size 2 starting from 2 till 100 i.e 2,4,6,...100


