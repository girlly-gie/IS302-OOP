#Fernandez Girlly
class Inventory:

    def __init__(self, name, price, quantity):
        self.name_gmf = name
        self.price_gmf = price
        self.quantity_gmf = quantity

    def get_product_info(self):
        return [self.name_gmf, self.price_gmf, self.quantity_gmf]

    def update_quantity(self, quantity):
        self.quantity_gmf += quantity

    def update_price(self, price):
        self.price_gmf += price

inventory_gmf = Inventory("Laptop", 45000, 10)
print(inventory_gmf.get_product_info())