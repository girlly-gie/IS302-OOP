# Fernandez,Girlly
grade_gmf = []

for i in range(5):
    name_gmf = input("Enter grade: ")
    grade_gmf.append(name_gmf)

print("\nStudent List")
for grade in grade_gmf:
    print(grade)

grade_gmf = {
    "Average grade": 86.6,
    "Highest grade": 92,
    "Lowest grade": 78
}

for grade, average in grade_gmf.items():
    print(grade, ":", average)