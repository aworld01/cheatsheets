class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def full_name(self):
        print(f"Name: {self.brand} {self.model}")
    def make_a_call(self, number):
        print(f"Calling {number}")

class Smartphone(Phone):
    def __init__(self, brand, model, price, ram, rom, camera):
        # Phone.__init__(self, brand, model, price) #uncommon
        super().__init__(brand, model, price) #common
        self.ram = ram
        self.rom = rom
        self.camera = camera

sphone = Smartphone("onePluse", 5, 30000, "6GB", "64GB", "20MP") #making instance
sphone.full_name() #calling full_name method
sphone.make_a_call(919006228083) #calling make_a_call method
