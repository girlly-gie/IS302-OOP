#Fernandez Girlly
class Employee:

    def __init__(self, name):
        self.__name_gmf = name
        self.__salary_gmf = 0

    def set_salary(self, salary):
        if salary > 0:
            self.__salary_gmf = salary

    def get_salary(self):
        return self.__salary_gmf

emp_gmf = Employee("Girlly")

emp_gmf.set_salary(30000)

print("Salary:", emp_gmf.get_salary())