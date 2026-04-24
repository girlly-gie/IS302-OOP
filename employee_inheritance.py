class Employee:

    def __init__(self, name, salary):
        self.name_gmf = name
        self.salary_gmf = salary

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department_gmf = department

    def display_manager(self):
        print("Name:", self.name_gmf)
        print("Salary:", self.salary_gmf)
        print("Department:", self.department_gmf)

manager1 = Manager("Girlly", 50000, "IS")
manager1.display_manager()