name=input("Enter your name: ")
n=len(name)
temp=""
for i in range(n):
    item=name[i]
    if item not in temp:
        temp+=item
        print(f"{item}: {name.count(item)}")