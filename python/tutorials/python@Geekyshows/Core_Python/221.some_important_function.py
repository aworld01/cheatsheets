"""
int(): This function returns an integer object or return 0 if no arguments are given.
Syntax:- int(a)

float(): This function returns an floating point number object.
Syntax:- float(a)

str(): This function returns str version of object.
Syntax:- str(a)

list(): Rather than being a function, list is actually a mutable sequence type. This can be used in type casting to convert iterable to list.
Syntax:- list(iterable)

tuple(): Rather than being a function, tuple is actually an immutable sequence type. This can be also used in type casting to convert iterable to tuple.
Syntax:- tuple(iterable)

set(): This function returns a new set object, optionally with elements taken from iterable. This can be also used in type casting to convert iterable to set.
Syntax:- set(iterable)

dict(): This function creates a new dictionary. This can be also used in type casting to convert iterable to dict.
Syntax:- dict(**kwarg)
"""


a = 10.56
print('Before type casting:',a,type(a))
new_a = int(a) #to convert 'float' into 'int'
print('After type casting:',new_a,type(new_a))
print()

b = '10'
print('Before type casting:',b,type(b))
new_b = int(b) #to convert 'str' into 'int', if content is convertable
print('After type casting:',new_b,type(new_b))
print()

c = 10
print('Before type casting:',c,type(c))
new_c = float(c) #to convert 'int' into 'float'
print('After type casting:',new_c,type(new_c))
print()

d = 10.56
print('Before type casting:',d,type(d))
new_d = int(d) #to convert 'float' into 'int'
print('After type casting:',new_d,type(new_d))
print()

e = 10
print('Before type casting:',e,type(e))
new_e = str(e) #to convert 'int' into 'str'
print('After type casting:',new_e,type(new_e))
print()

f = 10.56
print('Before type casting:',f,type(f))
new_f = str(f) #to convert 'float' into 'str'
print('After type casting:',new_f,type(new_f))
print()

g = (10,20,30)
print('Before type casting:',g,type(g))
new_g = list(g) #to convert 'tuple' into 'list'
print('After type casting:',new_g,type(new_g))
print()

h = {10,20,30}
print('Before type casting:',h,type(h))
new_h = list(h) #to convert 'set' into 'list'
print('After type casting:',new_h,type(new_h))
print()

i = 'ArtificialWorld'
print('Before type casting:',i,type(i))
new_i = list(i) #to convert 'str' into 'list'
print('After type casting:',new_i,type(new_i))
print()

j = {101:'Rahul',102:'Raj',103:'Sonam'}
print('Before type casting:',j,type(j))
new_j = list(j) #to convert 'dict' into 'list'
print('After type casting:',new_j,type(new_j))
print()

k = [10,20,30]
print('Before type casting:',k,type(k))
new_k = tuple(k) #to convert 'list' into 'tuple'
print('After type casting:',new_k,type(new_k))
print()

l = {10,20,30}
print('Before type casting:',l,type(l))
new_l = tuple(l) #to convert 'set' into 'tuple'
print('After type casting:',new_l,type(new_l))
print()

m = 'ArtificialWorld'
print('Before type casting:',m,type(m))
new_m = tuple(m) #to convert 'str' into 'tuple'
print('After type casting:',new_m,type(new_m))
print()

n = {101:'Rahul',102:'Raj',103:'Sonam'}
print('Before type casting:',n,type(n))
new_n = tuple(n) #to convert 'dict' into 'tuple'
print('After type casting:',new_n,type(new_n))
print()

o = [10,20,30]
print('Before type casting:',o,type(o))
new_o = set(o) #to convert 'list' into 'set'
print('After type casting:',new_o,type(new_o))
print()

p = (10,20,30)
print('Before type casting:',p,type(p))
new_p = set(p) #to convert 'tuple' into 'set'
print('After type casting:',new_p,type(new_p))
print()

q = 'ArtificialWorld'
print('Before type casting:',q,type(q))
new_q = set(q) #to convert 'str' into 'set'
print('After type casting:',new_q,type(new_q))
print()

r = {101:'Rahul',102:'Raj',103:'Sonam'}
print('Before type casting:',r,type(r))
new_r = set(r) #to convert 'dict' into 'set'
print('After type casting:',new_r,type(new_r))
print()

s = [(101,'Rahul'),(102,'Raj'),(103,'Sonam')]
print('Before type casting:',s,type(s))
new_s = dict(s) #to convert 'list' into 'dict'
print('After type casting:',new_s,type(new_s))
print()