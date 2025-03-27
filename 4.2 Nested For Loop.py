# Run the code and observe the output.
# Task: Modify the code to include 5 students and 4 classes

classes = ["Class A", "Class B", "Class C"]
students = ["Alice", "Bob", "Charlie"]

for class_name in classes:  # Outer loop for classes
    for student in students:  # Inner loop for students
        print(student, "is in", class_name)
