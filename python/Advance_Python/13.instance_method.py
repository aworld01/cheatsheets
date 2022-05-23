'''
There are three types of methods:
	1.Instance_methods
	2.Class_methods
	3.Static_methods
		
There are two types of instance_methods
	1.Accessor_methods
	2.Mutator_methods

Instance methods are the methods which act upon the instance variables of the class.
Instance_method need to know the memory address of the instance which is provided through self variable by default as first parameter of the instance_method.

Instance_methods are bound to object of the class so we call instance_method with object name.
2:30/13:50
'''

##Instance_method without Parameter/Formal_argument
#class Mobile():
#	def show(self):
#		print('RealMe X')
#		
#realme = Mobile()
#realme.show()


#class Mobile():
#	def __init__(self):
#		self.model = 'RealMe X' #instance_variable
#	def show(self): #instance_method
#		print('Model:', self.model)
#		
#realme = Mobile()
#realme.show()

##Instance_method with Parameter/Formal_argument
class Mobile():
	def __init__(self):
		self.model = 'RealMe X' #instance_variable
	def show(self, p): #instance_method
		self.price = p
		print('Model:', self.model)
		print('Price:', self.price)
		
realme = Mobile()
realme.show(5000)