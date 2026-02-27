string1 = 'Hello world!'
string2 = 'Hello world!'

c1 = string1 is string2
c2 = string1 == string2

print(c1, c2)
print(id(string1), id(string2))
print()




l1 = ['Apple', 'Mango', 'Orange']
l2 = ['Apple', 'Mango', 'Orange']

c1 = l1 is l2
c2 = l1 == l2

print(c1, c2)
print(id(l1), id(l2))