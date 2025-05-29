# student_marks.py

# Dictionary of student names and their marks
student_marks = {
    "Furqaan": 88,
    "Rehan": 76,
    "Talha": 91,
    "Saira": 84
}

# Ask the user for a name
name = input("Enter the student's name: ")

# Check if the name exists in the dictionary
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Oops! Couldn't find that student in the records.")
