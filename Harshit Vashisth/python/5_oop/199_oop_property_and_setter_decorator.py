"""Example-1"""
# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = max(price, 0) #to prevent negative price
#     def spec(self):
#         print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}")

# nok = Phone("Nokia", "1100", -1000)
# nok.spec()


"""Example-2 (property decorator)"""
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)

    @property #to convert a method into property
    def spec(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}")

nok = Phone("Nokia", "1100", -1000)
nok.spec