#Fernandez Girlly
class Person:

    def __init__(self, name, age):
        self.__name_gmf = name
        self.__age_gmf = age

    def get_name(self):
        return self.__name_gmf

    def get_age(self):
        return self.__age_gmf

p1 = Person("Girlly", 20)

print("Name:", p1.get_name())
print("Age:", p1.get_age())