import os
path = '.'
find = input('Find: ')
replace = input('Replace: ')
count = 0

for paths, dirs, files in os.walk(path):
  for file in files:
    old = os.path.join(paths, file)
    if file == 'file_editor.py':
      continue
    print("Conversion is going for >>", file)
    with open(old, mode='r', encoding='utf-8') as rf:
      data = rf.read()
      count += data.count(find)
      new = data.replace(find, replace)
      with open(old, mode='w', encoding='utf-8') as wf:
        wf.write(new)
print('Total file record replaced:', count)
     