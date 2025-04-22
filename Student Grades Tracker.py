# List of student names
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Dictionary of student grades
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eva": 88
}

# Simulate updating a grade
grades["Charlie"] = 82  # Updated grade

# Remove an absent student
students.remove("David")
grades.pop("David")

# Sort students alphabetically
students.sort()

# Slice top 3 students
top_3_students = students[:3]
print("Top 3 Students (Alphabetical):", top_3_students)
