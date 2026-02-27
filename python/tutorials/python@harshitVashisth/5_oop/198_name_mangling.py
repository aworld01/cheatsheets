class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price #name mangling

nokia = Phone("nokia", "1100", 1000)
print(nokia.__dict__) #to access instance property