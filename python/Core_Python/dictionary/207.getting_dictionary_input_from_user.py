a = {}
n = int(input("Enter the number of elements: "))
for i in range(n):
    key = input('Enter the key: ')
    value = input('Enter the value: ')
    a.update({key:value})
print(a)