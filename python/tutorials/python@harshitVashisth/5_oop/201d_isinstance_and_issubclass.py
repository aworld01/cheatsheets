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
    def full_spec(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"RAM: {self.ram}")
        print(f"ROM: {self.rom}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"Price: {self.price}")

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

ph = Smartphone("Samsung", "M31", 15000, "6GB", "128GB", "64MP")

"""isinstance(instance_name, class_name)"""
print(isinstance(ph, Phone))
print(isinstance(ph, FlagshipPhone))

"""issubclass(child_class, parent_class)"""
# print(issubclass(Phone, Smartphone))
# print(issubclass(Smartphone, Phone))