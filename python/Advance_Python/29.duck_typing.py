'''
In python, we follow a principle- If 'it walks like a duck and talks like a duck, it must be a duck' which means python doesn't care about which class of object it is, if it's an object and required behavior is present for that object then it will work. The type of object is distinguished only at runtime, This is called as duck typing.

Python doesn't care about which class of object it is, in order to call an existing method on an object. If the method is defined on the object, then it will be called.
'''

class Duck:
    def walk(self):
        print('thapak thapak thapak thapak')
class Horse:
    def walk(self):
        print('tabdak tabdak tabdak tabdak')

def myfunction(obj):
    obj.walk()

d = Duck()
myfunction(d)

h = Horse()
myfunction(h)