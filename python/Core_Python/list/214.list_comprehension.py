"""
Comprehension contains vary compact code usually a single statement that perform a task.

1: List comprehension
2: Set comprehension
3: Dictionary comprehension

List_comprehension: This represents creation of a new list from an iterable object that satify a given condition.

Syntax: new_list[comprehension for item in iterable_object if_statement]
Ex: l1 = [i+1 for i in range(20)]
Ex: l1 = [i for i in range(20) if i%2 == 0]
Ex: l1 = [i for i in range(20) if i%2 == 0 if i%3 == 0]
"""

#l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#l1 = []
#print('L:-',l)
#for i in l:
#  l1.append(i+1)
#print('L1:-',l1)

#l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#print('L:-',l)
#l1 = [i+1 for i in l]
#print('L1:-',l1)



#l1 = []
#for i in range(20):
#  l1.append(i+1)
#print('L1:-',l1)

#l = [i+1 for i in range(20)]
#print(l)



#l = []
#for i in range(20):
#  if i%2==0:
#    l.append(i)
#print(l)

#l = [i for i in range(20) if i%2==0]
#print('New_list: ',l)



#l = []
#for i in range(20):
#  if i%2==0:
#    if i%3==0:
#      l.append(i)
#print(l)

#l = [i for i in range(20) if i%2==0 if i%3==0]
#print('New_list: ',l)


"""
List comprehension with if-else statement
Sytax: l = [comprehension if_statement else_expression for item in iterable_object]
Ex: l = [i if i%2==0 else "invalid" for i in range(10)]
"""



l = []
for i in range(10):
  if i%2==0:
    l.append(i)
  else:
    l.append('Invalid')
print(l)