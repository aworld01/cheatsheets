'''
A class within a class is called as nested_class or nesting of a class or inner_class
'''

class Army: #outer_class
	def __init__(self):
		self.name = 'Rahul'
		self.gn = self.Gun() #creating inner_class object		
	def show(self):
		print('Name:', self.name)
		
	class Gun: #inner_class
		def __init__(self):
			self.name = 'AK 47'
			self.capacity = '75 Rounds'
			self.length = '34.3 inch'
		def disp(self):
			print('name:', self.name)
			print('Capicity', self.capacity)
			print('Length', self.length)			
#a = Army()

#print(a.name) #to access outer_class_variable
#a.show() #to access outer_class_method
#print()

#print(a.gn.name) #to access inner_class_variable
#a.gn.disp() #to access inner_class_method

#g = a.gn
#print(g.name)
#g.disp()



 #creating inner_class object outside
g = Army().Gun()
print(g.name)
g.disp()