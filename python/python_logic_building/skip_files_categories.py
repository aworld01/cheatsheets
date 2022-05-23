import os
path = '../.'
n = os.listdir(path)
skip = ('.txt', '.py')

for file in n:
  print(file)
print()

for file in n:
  if file.endswith(skip):
    continue
  print(file)