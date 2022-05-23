'''
When more than one method with the same name is defined in the same class, it's known as method overloading

In python, if a method is written such that it can perform more than one task is called method overloading.

We achieve method overloading by writing same method with several parameters.
'''
class Myclass:
	def sum(self, a=None, b=None, c=None):
		if a!=None and b!=None and c!=None:
			s = a+b+c
		elif a!=None and b!=None:
			s = a+b
		else:
			s = 'Provide at least two numbers'
		return s
obj = Myclass()

a = obj.sum(10, 20, 30)
print(a)

a = obj.sum(10, 20)
print(a)

a = obj.sum(10)
print(a)