import os
path = ('.')
replace = input('Enter the new file extension: ')
leave = ('html', 'py', 'js')
for paths, dirrs, files in os.walk(path):
  for file in files:
    if file == 'change_extension_recursive.py':
      continue
    if file.endswith(leave):
      continue
    path1 = os.path.join(paths, file)
    split = os.path.splitext(file)[0]
    new = split+'.'+replace
    path2 = os.path.join(paths, new)
    os.rename(path1, path2)
    print('\tConverting:', file, '->', new)
print("Task Done")