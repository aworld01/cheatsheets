winning_number = 43
guess = 1
number = int(input("Guess a number between 1-100: "))
game_over = False

while not game_over:
    if number==winning_number:
        print(f"\tYou win, and you guessed this number in {guess} times.")
        game_over = True
    else:
        if number<winning_number:
            print("\tToo low")
            guess+=1
            number = int(input("Guess again: "))
        else:
            print("\tToo high")
            guess+=1
            number = int(input("Guess again: "))