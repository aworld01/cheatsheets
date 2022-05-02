import os
path = '.'
source = os.listdir(path)
name ='file'
ext = 'jpg'
count = 1

for file in source:
  if file == 'rename.py':
    continue
  if os.path.isfile(file):
    new = name+'_'+str(count)+'.'+ext
    count += 1
    os.rename(file, new)
    print('\tConverting:', file, '->',new)
print("Total file renamed: ", count)