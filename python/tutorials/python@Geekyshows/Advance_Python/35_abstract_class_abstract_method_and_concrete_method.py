"""
A class derived from ABC class which belongs to abc module, is known as abstract class in Python.

ABC Class is known as Meta Class which means a class that defines the behavior of other classes. So we can say, Meta Class ABC defines that the class which is derived from it becomes an abstract class.

Abstract Class needs to be extended and its method implemented.

PVM can not create object of an abstract class.


ABSTRACT METHOD
A abstract method is a method whose action is redefined in the child classes as per the requirement of the object.
We can declare a method as abstract method by using @abstractmethod decorator.

Example (Abstract method / Method Without Body):-
    @abstractmethod
    def disp(self):
        pass

CONCRETE METHOD
A concrete method is a method whose action is defined in the abstract class itself.

Example (Concrete Method / Method with Body):-
    def show(self):
        print("Concrete Method")

RULES:
PVM can not create objects of an abstract class.
It is neccessary to declare all methods abstract in a abstract class.
Abstract Class can have abstract method and concrete methods.
If there is any abstract method in a class, that class must be abstract.
The abstract methods of an abstract class must be defined in its child class/subclass.
If you are inheriting any abstract class that have abstract method, you must either provide the implementation of the method or make this class abstract.

WHEN USE ABSTRACT CLASS
We use abstract class when there are some common feature shared by all the abject as they are.
"""
from abc import ABC, abstractmethod
"""example-1"""
# class Father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass
#     def show(self):
#         print("Concrete method...")
"""child-class"""
# class Child(Father):
#     def disp(self):
#         print("Child class...")
#         print("Defining Abstract Method...")
# c = Child()
# c.disp()
# c.show()



"""example-1"""
class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print("Gun = AK47")
"""child-class"""
class Army(DefenceForce):
    def area(self):
        print("Army Area = Land")
        print()
class AirForce(DefenceForce):
    def area(self):
        print("Airforce Area = Sky")
        print()
class Navy(DefenceForce):
    def area(self):
        print("Nave Area = Sea")
        print()
a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()

af.gun()
af.area()

n.gun()
n.area()