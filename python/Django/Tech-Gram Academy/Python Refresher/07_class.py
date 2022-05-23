##creating class
# class Dog:
#     pass

# my_dog=Dog() #creating object
# my_dog.name="Rocket"
# print(my_dog.name)




# class Dog:
#     name="Rocky" #class variable

# my_dog=Dog()
# your_dog=Dog()
# your_dog.name="Rocket" #to changing the class variable value but only for current object
# print(my_dog.name)
# print(your_dog.name)




# class Dog:
#     def bark(self):
#         print("bow bow")

# my_dog=Dog()
# my_dog.bark()




class Dog:
    def __init__(self, name, color, age):
        self.name=name
        self.age=age
        self.color=color

my_dog=Dog("Tiger", "Brown", 16)
your_dog=Dog("Ceaser", "White", 15)
print(my_dog.name)
print(your_dog.name)