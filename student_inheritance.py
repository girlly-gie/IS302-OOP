class Person:

    def __init__(self, name, age):
        self.name_gmf = name
        self.age_gmf = age

class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course_gmf = course

    def display_student(self):
        print("Name:", self.name_gmf)
        print("Age:", self.age_gmf)
        print("Course:", self.course_gmf)

student1_gmf = Student("Girlly", 20, "BSIS")
student1_gmf.display_student()