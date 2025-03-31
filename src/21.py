def calculate_average_grade(students):
    total_grades = sum([student['grade'] for student in students])
    average_grade = total_grades / len(students)
    return average_grade

students = [
    {
        "name": "Alice",
        "grade": 90,
        "classes": ["Math", "Science"],
        "subjects": ["History", "English"]
    },
    {
        "name": "Bob",
        "grade": 85,
        "classes": ["Art", "Music"],
        "subjects": ["English", "Geography"]
    }
]

average_grade = calculate_average_grade(students)
print(f"The average grade is: {average_grade}")
