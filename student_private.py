#Fernandez Girlly
class Student:

    def __init__(self, name, student_id, gpa):
        self.__name_gmf = name
        self.__student_id_gmf = student_id
        self.__gpa_gmf = gpa

    def get_student_info(self):
        print("Name:", self.__name_gmf)
        print("Student ID:", self.__student_id_gmf)
        print("GPA:", self.__gpa_gmf)

student1_gmf = Student("Juan", "2023-001", 1.75)
student1_gmf.get_student_info()