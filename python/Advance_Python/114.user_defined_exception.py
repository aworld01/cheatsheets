'''
A programmer can create his own exceptions, called user-defined exceptions or Custom Exception.

a.Creating Exception Class using Exception Class as a Base Class.
b.Raising Exception.
c.Handling Exception

CREATING EXCEPTION
We can create our own exception by creating a sub class to built-in Exception class.
Syntax:
class MyException(Exception):
    pass

RAISING EXCEPTION
raise statement is used to raise the user-defined exception.
Syntax:
raise MyException('message')

HANDLING EXCEPTION
Using try and except block Programmer can handle exceptions.
Syntax:
try:
    statement
except MyException as mye:
    statement

03:45/14:32
'''

# class BalanceException(Exception):
#     pass

# def checkbalance():
#     money = 10000
#     withdraw = 9000
#     try:
#         balance = money - withdraw
#         if (balance<=2000):
#             raise BalanceException('Insufficient Balance')
#         print(balance)
#     except BalanceException as be:
#         print(be)
# checkbalance()



class BalanceException(Exception):
    pass

def checkbalance():
    money = 10000
    withdraw = 5000
    balance = money - withdraw
    if (balance<=2000):
        raise BalanceException('Insufficient Balance')
    print(balance)

try:
    checkbalance()
except BalanceException as be:
    print(be)