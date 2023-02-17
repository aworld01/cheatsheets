class Student:
	# Constructor
	def __init__(self, n, r):
		self.name = n
		self.roll = r
	# Instance_method
	def disp(self):
		print('Student name:', self.name)
		print('Student roll:', self.roll)
		
class User:
	# Static_method
	@staticmethod
	def show(s):
		print('User name:', s.name)
		print('User roll:', s.roll)
		print()
		s.disp()
		
## creating object of Student_class
stu = Student('Rahul', 28)
User.show(stu)