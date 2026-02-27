class Product:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.name = f"{self.brand} {self.model}"
    def show(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Name: {self.name}")

mob = Product("Samsung","M31") #class_instance
lap = Product("HP","P45")

"""accessing variables"""
print("Mobile:")
print(mob.__dict__)
print()

print("Laptop:")
print(lap.__dict__)
print()