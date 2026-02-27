class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def full_name(self):
        print(self.brand, self.model)

# p1 = Phone("Nokia", 1100, 1200)
# p1.full_name()

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

# p2 = Smartphone("Samsung", "M31", 14000, "6GB", "128GB", "64MP")
# p2.full_name()
# p2.spec()

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

p3 = FlagshipPhone("Samsung", "M31", 14000, "6GB", "128GB", "64MP", "16MP")
p3.full_name()
p3.full_spec()