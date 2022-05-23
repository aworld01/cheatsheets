"""
Types of errors:-
1: SyntaxError
def func:
    print("Hello world")

SyntaxError: invalid syntax


2: IndentationError
def func():
print("Hello world")

IndentationError: expected an indented block


3: NameError
print(name)

NameError: name 'name' is not defined


4: TypeError
print(5+"Abdul")

TypeError: unsupported operand type(s) for +: 'int' and 'str'


5: IndexError
l = [1,2,3]
print(l[3])

IndexError: list index out of range


6: ValueError
l = "Abdul"
l = int(l)

ValueError: invalid literal for int() with base 10: 'Abdul'


7: AttributeError
l = [1,2,3]
l.push(13)

AttributeError: 'list' object has no attribute 'push'


8: KeyError
d = {"name": "Abdul"}
print(d["age"])

KeyError: 'age'


9: ZeroDivisionError
a = 5
b = 0
print(a/b)
print("Bye")

ZeroDivisionError: division by zero
"""

d = {"name": "Abdul"}
print(d["age"])

KeyError: 'age'