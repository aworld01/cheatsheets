'''
When we write a lambda function inside another lambda function that is called nested lambda function.
Ex:-
add = lambda x=10 : (lambda y : x+y)
a = add()
print(a(20))
'''
add = lambda x=10 : (lambda y : x+y)
a = add()
print(a)
print(a(20))