"""
ZeroDivisionError:-
a = 10
b = 0
print(a/b)
"""
"""example-1"""
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "You can't divide a number by zero"
# print(divide(10, 0))


"""example-2"""
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         return e
# print(divide(10, 0))


"""example-3"""
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return e
    except TypeError as e:
        return e
    except:
        return "Unexpected error.."
print(divide(10, "0"))
