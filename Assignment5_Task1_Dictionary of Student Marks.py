student_marks={"Alice": 85, "Bob": 90, "Charlie": 78, "David": 88, "Eve": 92}
Name=input("Enter the student's name: ")

if Name in student_marks:
    print(f"{Name}'s marks: {student_marks[Name]}")
else:
    print("Student not found.")

# This code snippet allows you to input a student's name and retrieve their marks from a predefined dictionary.