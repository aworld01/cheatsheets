class Laptop:
    discount = 10 #class variable
    def __init__(self, brand, model, price):
        """instance variables"""
        self.brand = brand
        self.model = model
        self.price = price
        self.name = f"{brand} {model}"
    def off(self):
        off_price = (Laptop.discount*self.price)/100
        print(f"Price: {self.price}")
        print(f"Discount: {off_price}")
        print(f"Total: {self.price-off_price}")

l1 = Laptop("HP", "AU114TX", 63000)
l2 = Laptop("Apple", "MacBook Pro", 230000)
l1.off()