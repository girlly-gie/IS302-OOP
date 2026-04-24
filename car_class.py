# Fernandez,Girlly
class Car:

    def __init__(self, brand, model, year):
        self.brand_gmf = brand
        self.model_gmf = model
        self.year_gmf = year

    def display_car(self):
        print(self.brand_gmf, self.model_gmf, self.year_gmf)

car1 = Car("Toyota", "Corolla", 2020)
car1.display_car()