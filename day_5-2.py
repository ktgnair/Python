# Write a program that calculates the highest score from a List of scores.
# You are not allowed to use the max or min functions.

student_scores = input("Input the scores of the students. ").split()

highest_score = 0
for score in student_scores:
    score_in_int = int(score)
    if highest_score < score_in_int:
        highest_score = score_in_int

print(f"The highest score in the class is {highest_score}")

