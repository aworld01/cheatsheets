import os
path = '.'
count = 0
find = input('Enter to find: ')
replace = input('Enter to replace: ')

for paths, dirs, files in os.walk(path):
  for file in files:
    if file =='replace_file_name_recursive.py':
      continue
    old = os.path.join(paths, file)
    count += file.count(find)
    new = file.replace(find, replace)
    os.rename(old, os.path.join(paths, new))
    print('\tConversion is going to: ', file, '>>', new)
print('Total renamed file is: ', count)