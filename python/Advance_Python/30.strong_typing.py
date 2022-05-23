'''
We can check whether the object passed to the method has the method being invoked or not.

hasattr() Function is used to check whether the object has a method or not.
Syntax: hasattr(object, 'attribute')

Where attribute can be a method or variable. If it's found in the object then this method returns True else False.
'''

class Duck:
    def walk(self):
        print('thapak thapak thapak thapak')
class Horse:
    def walk(self):
        print('tabdak tabdak tabdak tabdak')
class Cat:
    def talk(self):
        print('Meow Meow')


def myfunction(obj):
    if hasattr(obj, 'walk'):
        obj.walk()
    elif hasattr(obj, 'talk'):
        obj.talk()

d = Duck()
myfunction(d)

h = Horse()
myfunction(h)

t = Cat()
myfunction(t)