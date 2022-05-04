import os
path = ('.')
count = 0

for path, folders, files in os.walk(path):
  for file in files:
    if file == 'count.py':
      continue
    count += file.count(file)
    print(file)
  
print('\tTotal files: ', count)