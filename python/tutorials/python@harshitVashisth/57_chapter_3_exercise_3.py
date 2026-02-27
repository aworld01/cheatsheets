number=input("Enter a number containing more than one digit: ")
n=len(number)
total=0
i=0
while i<n:
    total+=int(number[i])
    i+=1
print(total)
