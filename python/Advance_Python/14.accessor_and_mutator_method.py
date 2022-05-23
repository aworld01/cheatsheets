'''
Accessor_method::::
This method is used to access or read data of the variable.
This method do not modify the data in the variable.
This is also called as getter_method
Ex:
	def get_value(self):
	def get_result(self):
	def get_name(self):
	def get_id(self):
		
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'
	
	def get_model(self):
		return 'RealMe 2'
		
realme = Mobile()
m = realme.get_model()
'''

'''
Mutator_method::::
This method is used to access or read and modify data of variables.
This is also called as setter_method
Ex:
	def set_value(self):
	def set_result(self):
	def set_name(self):
	def set_id(self):
		
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'
	
	def set_model(self):
		self.model = 'RealMe 2'
		
realme = Mobile()
s = realme.set_model()
'''


#class Mobile:
#	def __init__(self):
#		self.model = 'RealMe X'
#	#Getter_method
#	def get_model(self):
#		return self.model
#realme = Mobile()
#g = realme.get_model()
#print(g)



class Mobile:
	def __init__(self):
		self.model = 'RealMe X'
	#Setter_method
	def set_model(self):
		self.model = 'RealMe 2'
		
realme = Mobile()
#Before setting
before = realme.model
print(before)
#After setting
realme.set_model()
after = realme.model
print(after)