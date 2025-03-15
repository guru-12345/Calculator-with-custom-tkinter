#Run the code and observe the output.
#Task 1- Modify the code to greet 5 rows of students, with 6 students in each row.

for row in range(1, 4):  # Outer loop for rows (1 to 3)
    for student in range(1, 5):  # Inner loop for students (1 to 4)
        print("Hello Student", student, "in Row", row, "!")
