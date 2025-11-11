#A program to calculate the highest score from a list of scores.
student_scores = input("Input a list of student scores\n ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

Highest_score = 0

for score in student_scores:
    Get_score = score
    #Get_score = scor
    if Get_score >  Highest_score:
        Highest_score = Get_score
print(f"The highest value is:  { Highest_score} ")


