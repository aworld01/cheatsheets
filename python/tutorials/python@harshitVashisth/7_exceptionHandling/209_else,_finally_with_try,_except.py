"""
else: block runs if try runs successfully
finally: block always runs
"""

while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("\tInvalid input...")
    else:
        break
    finally:
        print("\tThis is finally block example...")
if age < 18:
    print("\tYou can't play the game...")
else:
    print("\tYou can play the game....")