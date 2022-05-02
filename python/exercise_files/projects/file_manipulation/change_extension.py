import os
path = os.listdir('.')
replace = input('Enter the new extension: ')
count = 0

for file in path:
  if file =='change_extension.py':
    continue
  if os.path.isfile(file):
    split = os.path.splitext(file)[0]
    new = split + '.' + replace
    os.rename(file, new)
    print('\tConverting:', file, '->', new)
print('Task done...')