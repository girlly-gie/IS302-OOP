class Animal:

    def __init__(self, name):
        self.name_gmf = name

    def speak(self):
        print(self.name_gmf, "makes a sound")

class Dog(Animal):

    def bark(self):
        print(self.name_gmf, "barks")

dog1 = Dog("Yunna")

dog1.speak()
dog1.bark()