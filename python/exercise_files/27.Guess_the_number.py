n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times:")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number: "))
    if guess_number < 18:
        print("You enter less number please input greater number: \n")
    elif guess_number > 18:
        print("You enter greater number please input smaller number: \n")
    else:
        print("Congratulations, you won !!!")
        print("You took to finish: ", number_of_guesses, "number of guesses.")

        break
    print(9 - number_of_guesses,"number of guesses left.")
    number_of_guesses += 1
if (number_of_guesses > 9):
    print("Game over......")