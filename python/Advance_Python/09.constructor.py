#class Mobile:
#	def __init__(self):
#		print("Mobile constructor called")
#realme = Mobile()
#redmi = Mobile()
#oppo = Mobile()



#class Mobile:
#	## constructor without parameter
#	def __init__(self):
#		self.model = "Realme X"
#		
#	def show(self):
#		print("Model: ", self.model)
#realme = Mobile()
#realme.show()



#class Mobile:
#	## constructor with parameter
#	def __init__(self, m, p):
#		self.model = m
#		self.price = p
#		
#	def show(self):
#		print(f"Model: {self.model}\nPrice: {self.price}")
#		print()
#		
##passing argument to constructor		
#realme = Mobile("Realme X", 5500)
#nokia = Mobile("Nokia 3310", 2400)
##accessing method from outside class
#realme.show()
#nokia.show()



#class Mobile:
#	## constructor with default parameter
#	def __init__(self, m, v=80):
#			self.model = m
#			self.volumn = v
#			
#	def show(self, p):
#			price = p #local variable
#			print(f"Model: {self.model}\nVolumn: {self.volumn}\nPrice: {price}")
#			print()

##passing argument to constructor
#realme = Mobile("Realme X") #not passing argument for v
##accessing method from outside class
#realme.show(5000)

#redmi = Mobile("Redmi 7", 50) #passing argument for v
#redmi.show(8000)