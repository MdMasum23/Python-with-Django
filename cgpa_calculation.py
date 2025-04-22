# University CGPA Calculator

# Grade to point mapping
grade_points = {
    "A+": 4.0,
    "A": 3.75,
    "A-": 3.5,
    "B+": 3.25,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "F": 0.0
}

# Get number of courses
n = int(input("Enter total number of courses: "))

total_credits = 0
total_points = 0

for i in range(n):
    print(f"\nCourse {i+1}:")
    credit = float(input("  Enter course credit: "))
    grade = input("  Enter your grade (A+, A, A-, etc.): ").upper()

    if grade in grade_points:
        point = grade_points[grade]
        total_credits += credit
        total_points += credit * point
    else:
        print("  ❌ Invalid grade. Skipping this course.")

# Calculate CGPA
if total_credits > 0:
    cgpa = total_points / total_credits
    print(f"\n🎓 Your CGPA is: {cgpa:.2f}")
else:
    print("❌ No valid courses entered.")
