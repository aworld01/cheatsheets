import os
path = ('.')
n = os.listdir(path)

print('All files and dirs.')
## to access all files and dirs
for file in n:
  print('\t',file)
print()
  
print('Only files')
## to access only file
for file in n:
  new = os.path.join(path, file)
  if os.path.isfile(new):
      print('\t',file)
print()
  
  
print('Only directories')
## to access only dir
for dir in n:
  new = os.path.join(path, dir)
  if os.path.isdir(new):
      print('\t',dir)