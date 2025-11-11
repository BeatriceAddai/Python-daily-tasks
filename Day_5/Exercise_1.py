#Average height exercise
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

Add_height = 0
for height in student_heights:
    Add_height += height
print( Add_height )

number_of_students = 0
for students in student_heights:
    number_of_students += 1

    Average =  Add_height/ number_of_students
print( Average )