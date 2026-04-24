class Vehicle:

    def __init__(self, brand, model):
        self.brand_gmf = brand
        self.model_gmf = model

class Car(Vehicle):

    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year_gmf = year

    def display_car(self):
        print(self.brand_gmf, self.model_gmf, self.year_gmf)

car1 = Car("Toyota", "Corolla", 2022)
car1.display_car()