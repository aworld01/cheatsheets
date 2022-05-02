while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("\tInvalid input: ")

if age < 18:
    print("\tYou can't play the game...")
else:
    print("\tYou can play the game....")