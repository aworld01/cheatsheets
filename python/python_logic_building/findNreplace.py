find = 'abDul Zoha'.lower()
replace = 'Neo'
result = 0

with open('test.txt', mode='r', encoding='utf-8') as rf:
  for data in rf.readlines():
    print(data)
print('\n')

with open('test.txt', mode='r', encoding='utf-8') as rf:
  for data in rf.readlines():
    l = data.lower()
    data = l.replace(find, replace)
    result += data.count(replace)
    print('\t', data.lower())
print('Total replaced: ', result)