"""
Create a Laptop class with attributes like brand_name, model_name and price.

Create two objects/instance of your laptop class
"""
class Laptop:
    def __init__(self, brand, model, price):
        """instance variables"""
        self.brand = brand
        self.model = model
        self.price = price
        self.name = brand+" "+model

dell = Laptop("Dell", "Insprion 15", 18000)
hp = Laptop("HP", "AU114TX", 63000)

print(dell.brand)
print(hp.name)