'''
We can access class variable using class_name.variable_name

'''

class Mobile:
	fp = 'yes' #class variable
	
	@classmethod #class method
	def show(cls):
	  print(cls.fp) #accessing class variable inside class method
	  
Mobile.show() #to call class method
print(Mobile.fp) #accesssing class variable outside class method

Mobile.fp = 'no' #to modify class variable outside the class
print(Mobile.fp)