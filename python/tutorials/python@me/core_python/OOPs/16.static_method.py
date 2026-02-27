'''
Static_methods are used when some processing is related to the class but does not need the class or its instances to perform any work.

We use static_method when we want to pass some values from outside and perform some action in the method.

Decorator @staticmethod need to write above the static_method.
'''

##Static_method W/O formal-argument
#class Mobile:
#	fp = 'Yes' #class_variable
#	@staticmethod #decorator
#	def show(): #static_method
#		print('RealMe X')
#		print('Fingerprint:', Mobile.fp)
#		
#realme = Mobile()
#Mobile.show() #calling static method



##Static_method with formal-argument
class Mobile:
	fp = 'Yes' #class_variable
	@staticmethod #decorator
	def show(m, p): #static_method
		model = m
		price = p
		print('Model:', model, '\nPrice:', price)
		
realme = Mobile()
Mobile.show('Realme X', 3000) #calling static method