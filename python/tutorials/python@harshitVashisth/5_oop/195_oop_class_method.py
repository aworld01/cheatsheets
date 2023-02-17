class Person:
    count_instance = 0
    def __init__(self):
        Person.count_instance += 1
    @classmethod
    def count_instances(cls):
        print(f"You have created {cls.count_instance} instances of {cls.__name__} class...")

"""creating instances"""        
p1 = Person()
p2 = Person()

"""calling class method"""
Person.count_instances()
