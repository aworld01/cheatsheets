"""Apply dicount"""
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def discount(self, disc):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)
        d = self.price*disc/100
        print("Discound: ", d)
        print("Total: ", self.price - d)
        print()

dell = Laptop("Dell", "Insprion 15", 18000)
hp = Laptop("HP", "AU114TX", 63000)

dell.discount(35)
hp.discount(20)