number=input("Enter any three digit number: ")
n=len(number)
total=0
for i in range(n):
    total+=int(number[i])
print(total)