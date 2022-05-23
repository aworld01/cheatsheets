'''
In Python, Namespace represents a memory block where names are mapped to objects

There are two types of Namespaces
1.Class Namespace
2.Instance Namespace

Class namespace: A class maintains it's own namespace known as class_namespace.
In the class_namespace, the names are mapped to class_variables.

Instance namespace: Every Instance has it's own  namespace known as instance_namespace.
In the instance_namespace, the names are mapped to instance_variables.
'''

class Mobile:
	fp = 'Yes' #class_variable ('Yes' is a class_namespace)
	
	@classmethod #class_method
	def is_fp(cls):
		print('Fingerprint', cls.fp) #accessing class_variable
		
##objects
realme = Mobile() #'realme' is a instance_namespace
redmi = Mobile() #'redmi' is a instance_namespace
geek = Mobile() #'geek' is a instance_namespace

print('Class FP:', Mobile.fp)
print('Realme:', realme.fp)
print('Redmi:', redmi.fp)
print('Geek:', geek.fp)
print()

Mobile.fp = 'No' #modify value using class

print('Class FP:', Mobile.fp)
print('Realme:', realme.fp)
print('Redmi:', redmi.fp)
print('Geek:', geek.fp)
print()

realme.fp = 'Yes' #modify value using class

print('Class FP:', Mobile.fp)
print('Realme:', realme.fp)
print('Redmi:', redmi.fp)
print('Geek:', geek.fp)