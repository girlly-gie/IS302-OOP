# Fernandez,Girlly
class Student:

    def __init__(self, name, student_id, course):
        self.name_gmf = name
        self.student_id_gmf = student_id
        self.course_gmf = course

    def display_student(self):
        print("Name:", self.name_gmf)
        print("Student ID:", self.student_id_gmf)
        print("Course:", self.course_gmf)

student1 = Student("Girlly", "24-0003269", "BSIS")
student1.display_student()