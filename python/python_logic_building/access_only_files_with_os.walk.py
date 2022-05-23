import os
source = ('.')

for path, folder, file in os.walk(source):
  for f in file:
    print(f)
print()

for path, folder, file in os.walk(source):
  for d in folder:
    print(d)