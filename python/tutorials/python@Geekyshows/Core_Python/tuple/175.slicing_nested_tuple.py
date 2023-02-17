x = ((10,20,30),
    (30,40,50),
    (60,70,80),
    (21,22,23),
    (44,55,66),
    (77,88,99),
    (12,13,14))
print(f'Original tuple:\n{x}')
print()

a = x[0:]
print(f'From 0th position to last position:\n{a}')
print()

b = x[1:5]
print(f'From 1st position to 4th position:\n{b}')
print()

c = x[:5]
print(f'From 0th position to 4th position:\n{c}')
print()

d = x[-4:]
print(f'Last 4 tuple:\n{d}')
print()

e = x[0:7:2]
print(f'From 0th position to 6th position stepsize 2:\n{e}')
print()

f = x[-5:-3]
print(f'Last 5 tuple with [-5-(-3)]= 2 lists towards right:\n{f}')
print()

g = x[2:3]
print(f'Slice nested 2nd position, 0th position:\n{g}')
g2 = x[2:3][0]
print(g2)
print()

#Extracting only one element
h = x[2:3][0][0]
print(f'Slice 2nd tuple then extract elements:\n{h}')
print()

#Extracting all elements
z = x[2:3][0]
for i in z:
  print(i)
print()
  
j = x[-4:]
print(f'Last 4 elements:\n{j}')
print()

j1 = x[-4:][1]
print(f'1st index of last 4 elements:\n{j1}')
print()

k = x[-4:][1][0]
print(f'Last nested 4 lists then 1st position then extract elements:\n{k}')
print()

l = x[-4:][1]
for i in l:
  print(i)