#class Myclass(object):
#	def show(self):
#		print("I am method")
#x = Myclass()
#x.show()

#class Myclass:
#	def show(self):
#		print("I am method")
#x = Myclass()
#x.show()

#class Mobile:
#	def __init__(self):
#		self.model = "RealMe X"
#	def show(self):
#		print("Model: ",self.model)
#realme = Mobile()
#realme.show()

#class Mobile:
#	def __init__(self):
#		self.model = "RealMe X"
#	def show(self):
#		print("Model: ",self.model)
#realme = Mobile()
#print(realme.model) #to access the model outsde of class

#class Mobile:
#	def __init__(self):
#		self.model = "RealMe X"
#	def show(self):
#		print("Model: ",self.model)
#realme = Mobile()
#realme.show()
#realme.model = "RealMe pro2" #to re-assign model
#realme.show()

class Mobile:
	def __init__(self, m, r, p):
		self.model = m
		self.ram = r
		self.price = p
	def show(self):
		print(f"""Model: {self.model}
RAM: {self.ram}
Price: {self.price}""")
realme = Mobile("RealMe X", "4GB", 7000)
realme.show() #to access the model outsde of class