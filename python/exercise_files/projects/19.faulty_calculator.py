

def calculator():
    print("\nWelcome to Faulty Calculator: This is developed by Subham Roy....")
    operation = input('''
    Please type in the math operation you would like to complete
    + for Addition
    - for Subtraction
    * for Multiplication
    / for Division
    % for Modulo
    ** for Power

    Enter your choice: ''')

    num1 = int(input("Enter the 1st Number: "))
    num2 = int(input("Enter the 2nd Number: "))

    if operation == "+":
        if num1 == 56:
            print('56 + 9 = 77')
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        if num1 == 45:
            print("45 * 3 = 555")
        else:
            print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num1 == 56:
            print("56 / 6 = 4")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    elif operation == "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    elif operation == "%":
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Error! Please check your input")
    again()
def again():
    cal_again = input('''
    Do you want to calculate again?
    Please type y for YES or n for NO.
    ''')

    if cal_again == 'y':
        calculator()
    elif cal_again == 'n':
        print("See you later")
    else:
        again()
calculator()
