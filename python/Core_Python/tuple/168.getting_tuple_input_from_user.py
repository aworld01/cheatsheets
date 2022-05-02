a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    a.append(int(input("Enter Element: ")))
print(a, type(a))
a = tuple(a) #to conver list into tuple
print(a, type(a))