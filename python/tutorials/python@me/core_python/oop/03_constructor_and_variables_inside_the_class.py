"""constructor always called when we create instance of class"""
# class A:
#     def __init__(self):
#         print("Constructor called...")
# """creating instances"""
# a = A()
# b = A()



class A:
    gender = "male" #class_variable
    def __init__(self):
        self.name = "Abdul Zoha" #instance_variable
a = A()

"""accessing class and instance items"""
print("\tBefore updating")
print(A.__dict__)
print(a.__dict__)
print()

"""updating_variables outside the class"""
A.gender = "female"
a.name = "Tabassum Khatoon"

"""accessing class and instance items"""
print("\tAfter updating")
print(A.__dict__)
print(a.__dict__)
print()