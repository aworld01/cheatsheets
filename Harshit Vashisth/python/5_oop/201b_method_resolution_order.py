class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def full_name(self):
        print(self.brand, self.model)

class Smartphone(Phone):
    def __init__(self, brand, model, price, ram, rom, rear_camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.rom = rom
        self.rear_camera = rear_camera
    def spec(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"RAM: {self.ram}")
        print(f"ROM: {self.rom}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"Price: {self.price}")

# print(help(Smartphone)) #to check "Method Resolution Order (MRO)"

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, price, ram, rom, rear_camera, front_camera):
        super().__init__(brand, model, price, ram, rom, rear_camera)
        self.front_camera = front_camera
    def full_spec(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"RAM: {self.ram}")
        print(f"ROM: {self.rom}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Price: {self.price}")

print(help(FlagshipPhone)) #to check "Method Resolution Order (MRO)"