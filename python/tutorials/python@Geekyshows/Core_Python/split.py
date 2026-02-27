import os
path='.'
path2  = os.listdir(path)

##to get only file_name
#for file in path2:
#  if not (file == 'split.py'):
#    f=os.path.join(path, file)
#    if os.path.isfile(f):
#      extention = file.split('.')[0]
#      print(extention)
#print()

##to get only extention
#for file in path2:
#  if not (file == 'split.py'):
#    f=os.path.join(path, file)
#    if os.path.isfile(f):
#      extention = file.split('.')[1]
#      print(extention)
#print()

##to get file_name and extention
#for file in path2:
#  if not (file == 'split.py'):
#    f=os.path.join(path, file)
#    if os.path.isfile(f):
#      file, extention = file.split('.')
#      print(f'{file} => {extention}')

##to get only file_name by os module
for file in path2:
  if not (file == 'split.py'):
    f=os.path.join(path, file)
    if os.path.isfile(f):
      file, extention = os.path.splitext(file)
      print(f'{file} => {extention}')
print()