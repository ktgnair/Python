# Grading Program
# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the students are their exam scores.
# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for students. 
# The final version of the student_grades dictionary will be checked.

student_scores = {
    "Goutham": 82,
    "Rocky": 85,
    "Vinod": 75,
    "Bijo": 78,
    "Akshay": 68,
    "Abhijeet": 62,
    "Sanchit": 92,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 91 and student_scores[student] < 100:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 81 and student_scores[student] < 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 71 and student_scores[student] < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Needs Improvement"

print(student_grades)