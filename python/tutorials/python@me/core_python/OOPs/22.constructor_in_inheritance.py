'''
By default, the constructor in the Parent_class is available to the Child_class
'''
#class Father:
#	def __init__(self):
#		self.money = 1000
#		print('Father class constructor called:')
#		
#	def show(self):
#		print('Father class instance method')
#		
#class Son(Father):
#	def disp(self):
#		print('Son class instance method', self.money)

#s = Son()
#print(s.money)
#s.show()
#s.disp()


class Father:
	def __init__(self, m):
		self.money = m
		print('Father class constructor called:')
		
	def show(self):
		print('Father class instance method')
		
class Son(Father):
	def disp(self):
		print('Son class instance method', self.money+200)

s = Son(2000)
print(s.money)
s.show()
s.disp()