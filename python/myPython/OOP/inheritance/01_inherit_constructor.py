class A:
    def __init__(self, name, model, battary):
        self.name = name
        self.model = model
        self.battary = battary
    def details(self):
        print(f"Brand: {self.name}")
        print(f"Model: {self.model}")
        print(f"Battary: {self.battary}")
class B(A):
    def android(self):
        print(f"Oprating system: Android")
        print(f"Model: {self.model}")
        print(f"Battary: {self.battary}")
    
b = B("Nokia", 3310, "200mah")
b.details()
print()
b.android()