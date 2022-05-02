import os
path = ('.')
count = 0

for p_path, p_dir, p_file in os.walk(path):
  for file in p_file:
    if file == 'count.py':
      continue
    count += file.count(file)
    print(file)
  
print('\tTotal files: ', count)