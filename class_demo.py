# Fernandez,Girlly
class Person:
    def __init__(self, name, age):
        self.name_gmf = name
        self.age_gmf = age

    def display_info(self):
        print("Name:", self.name_gmf)
        print("Age:", self.age_gmf)

p1 = Person("Girlly", 20)
p1.display_info()