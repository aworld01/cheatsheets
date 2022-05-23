'''
Instance variables are the variables whose separate copy is created in every objects.

Instance variables are defined and initialized using a constructer with self parameter.

We can access instance variable out side the class using object_name.variable_name
'''

class Mobile:
	def __init__(self):
		self.model = 'RealMe X' #Instance variable
	def show(self):
		p = self.model #Accessing instance variable inside the class
		print(p)		
		q = self.model = 'Redme 7i' #re-assign value inside the class
		print(q)	
		
##Creating objects for instance_variable
realme = Mobile()
redme = Mobile()
artificial = Mobile()
##Accessing Instance variable outside the class using object_name.variable_name
a = realme.model
b = redme.model
c = artificial.model
print(a, b, c)
d = artificial.model = 'Nokia-3310' #re-assign value outside the class
print(a, b, d)