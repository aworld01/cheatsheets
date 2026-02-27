# class Laptop:
#     discount = 10 #class variable
#     def __init__(self, brand, model, price):
#         """instance variables"""
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.name = f"{brand} {model}"
#     def off(self):
#         off_price = (Laptop.discount*self.price)/100
#         print(f"Price: {self.price}")
#         print(f"Discount: {off_price}")
#         print(f"Total: {self.price-off_price}")

# l1 = Laptop("HP", "AU114TX", 63000)
# l2 = Laptop("Apple", "MacBook Pro", 230000)
# l2.off()

# Laptop.discount = 0 #to change class_variable for all objects

# l1.off()
# print()
# l2.off()

"""to print object property"""
# print(l1.__dict__)
# print(l2.__dict__)

# l2.discount = 5000 #this will make a new instance variable

# print(l2.__dict__)




"""final result"""
class Laptop:
    discount = 10 #class variable
    def __init__(self, brand, model, price):
        """instance variables"""
        self.brand = brand
        self.model = model
        self.price = price
        self.name = f"{brand} {model}"
    def off(self):
        off_price = (self.discount*self.price)/100 #to change value anytime
        print(f"Price: {self.price}")
        print(f"Discount: {off_price}")
        print(f"Total: {self.price-off_price}")



l1 = Laptop("HP", "AU114TX", 63000)
l2 = Laptop("Apple", "MacBook Pro", 230000)
l2.off()
print()

l2.discount = 50
print(Laptop.discount)
print(l2.__dict__)
print()

l2.off()