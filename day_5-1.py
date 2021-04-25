# Write a program that calculates the average student height from a List of heights.
# You should not use the sum() or len() functions in your answer. 
# You should try to replicate their functionality using what you have learnt about for loops.

# split() will return the output in list data structure
student_heights = input("Input the list of student heights. ").split()

total_height = 0
number_of_students = 0

for student in student_heights:
    number_of_students += 1
    total_height += int(student)
print(f"The Total sum is {total_height}")

total_average = round(total_height / number_of_students)
print(f"The Average height is {total_average}")
