students = {} #empty dictionary

while True:
    key = input("Please Enter your name: ")
    if (key == "exit") or (key == "quit"):
        break
    else:
        value = int(input("Enter your age: "))
        students.update({key:value}) #to update dictionary
        print(f"\t{students}")