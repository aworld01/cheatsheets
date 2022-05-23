'''
Class_methods are the methods which act upon the class_variables or static_variable of the class.

Decorator @classmethod need to write above the class_method

By default, the frist parameter of class_method is cls which refers to the class itself.
'''

##class_method W/O parameter
#class Mobile:
#	@classmethod #decorator
#	def show_model(cls): #class_method
#		print('RealMe X')
#realme = Mobile()
#Mobile.show_model() #calling class_method


#class Mobile:
#	fp = 'Yes' #class_variable
#	
#	@classmethod
#	def show_model(cls): #class_method
#		print('Fingerprint:', cls.fp)
#		
#realme = Mobile()
#Mobile.show_model()



##class_method W/O parameter
class Mobile:
	fp = 'Yes' #class_variable
	
	@classmethod
	def show_model(cls, r): #class_method
		cls.ram = r
		print('Fingerprint:', cls.fp)
		print('RAM:', cls.ram)
		
realme = Mobile()
Mobile.show_model('8GB')