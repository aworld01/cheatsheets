while True:
    try:
        age=int(input("Please enter your age: "))
        break
    except:
        print("Invalid input")
if age<18:
    print("You can't play this game.")
else:
    print("You can play this game.")