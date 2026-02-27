from database import*
import os

while True:
    user_input = int(input("""Choose what you want?
        1.Check tables
        2.Insert record
        3.Update record
        4.Delete record
        5.Exit
> """))
    if user_input == 1:
        show()

    elif user_input == 2:
        name = input("Enter your name: ")
        s_class = input("Enter your class: ")
        email = input("Enter your email: ")
        insert(name, s_class, email)

    elif user_input == 3:
        name = input("Enter your name: ")
        s_class = input("Enter your class: ")
        email = input("Enter your email: ")
        s_id = int(input("Please enter the id to update: "))
        update(name, s_class, email, s_id)
        print()

    elif user_input == 4:
        s_id = int(input("Enter the id to delete data: "))
        delete(s_id)
        print()

    elif user_input == 5:
        print("\tThank you for using the application:)")
        break

    else:
        print("\tPlease choose a correct option....")
        print()