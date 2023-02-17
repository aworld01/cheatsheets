# # Return statement Single Value
# # Defining a Function
# def add():
#     x = 10
#     y = 20
#     c = x + y
#     return c
# # Calling a function
# a = add()
# print(a)


# def add():
#     x = 10
#     y = 20
#     return x + y
# a = add()
# print(a)


# def add(y):
#     x = 10
#     return x + y
# a = add(30)
# print(a)




# # Return statement Multiple Value
# # Defining a Function
# def cal(y):
#     x = 10
#     c = x + y
#     d = y - x
#     return c, d
# # Calling a function
# sum,sub = cal(20)
# print(sub)
# print(sum)


def cal(y):
    x = 10
    c = x + y
    d = y - x
    return c, d, 50
sum,sub,a= cal(20)
print(sub)
print(sum)
print(a)