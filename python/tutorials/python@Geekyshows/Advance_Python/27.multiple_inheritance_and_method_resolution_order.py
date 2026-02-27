'''
If a class is derived from more than one parent class, then it's called multiple_inheritance'
Method Resolution Order (MRO)

In the multiple_inheritance scenario members of class are searched first in the current_class. If not found, the search continues into parent classes in depth first left to right manner without searching the same class twice.

Search for the child class before going to its parent class.
When a class is inherited from several classes, it searches in the order from left to right in the parent classes.
It will not visit any class more than once which means a class in the inheritance hierarchy is traversed only once exactly.
'''
#class Father:
#		def showF(self):
#			print('Father class method')
#		
#class Mother:
#		def showM(self):
#			print('Mother class method')
#		
#class Son(Father, Mother):			
#		def showS(self):
#			print('Son class method')
#		
#s = Son()
#s.showS()
#s.showM()
#s.showF()




'''
s = Son()
The search will start from Son. As the object of Son is created, the constructor of Son is called.
Son has super().__init__() inside his constructor so its parent class, the one in the left side 'Father' class's constructor is called.
Father class also has super().__init__() inside  his constructor so its parent 'object' class's constructor is called.
object doesn't have any constructor so the search will continue down to right hand side class (Mother) of object class so Mother class's constructor is called.
As Mother class also has super().__init__() so its parent class 'object' constructor is called but as object class already visited, the search will stop here.
'''
class Father:
		def __init__(self):
			super().__init__() #calling parent class constructor
			print('Father class constructor')
			
		def showF(self):
			print('Father class method')
		
class Mother:
		def __init__(self):
			super().__init__() #calling parent class constructor
			print('Mother class constructor')
		
		def showM(self):
			print('Mother class method')
		
class Son(Father, Mother):
		def __init__(self):
			super().__init__() #calling parent class constructor
			print('Son class constructor')
			
		def showS(self):
			print('Son class method')
		
s = Son()