class Computer:
    def config(self):
        print("i5, 16GB, 1TB")

"""example-1"""
# Computer.config("comp1")
# Computer.config("comp2")

"""example-2"""
"""creating instance"""
comp1 = Computer() #instance
comp2 = Computer()

"""calling methods"""
comp1.config()
comp2.config()