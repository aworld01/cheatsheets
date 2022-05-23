import os
path = '.'
count = 0
find = input('Enter to find: ')
replace = input('Enter to replace: ')

for file in os.listdir(path):
  if file == 'replace_file_name.py':
    continue
  count += file.count(find)
  new = file.replace(find, replace).lower()
  os.rename(file, new)
  print('Conversion is going to: ', file, '>>', new)
  
print('Total renamed:', count)