'''
If we write constructor in the both classes, parent_class and child_class then the parent class constructor is not available to the child_class.
In this case only child_class constructor is accessible which means child_class constructor is replacing parent_class constructor.
Constructor_overriding is used when programmer want to modify the existing behavior of a constructor.
'''

class Father:
	def __init__(self):
		self.money = 2000
		self.car = 'BMW'
		print('Father class constructor')
		
	def show(self):
			print('Father class instance method')
			
class Son(Father):
	def __init__(self):
		self.money = 5000
		self.car = 'Ferrari'
		print('Son class constructor')
		
	def disp(self):
		print('Son class instance method')
		
s = Son()
print(s.money)
print(s.car)
s.disp()
s.show()