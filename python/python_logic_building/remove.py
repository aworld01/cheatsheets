import os
path = '../.'
n = os.listdir(path)

for file in n:
  print(file)
print()

n.remove('python_logic_building')
for file in n:
  print(file)