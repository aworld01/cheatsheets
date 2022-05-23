# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     else:
#         print("Oops you are passing wrong datatype.")
# a=add(2, "5")
# print(a)



def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("Oops you are passing wrong datatype.")
    # raise ValueError("Oops you are passing wrong datatype.")
a=add("2", "5")
# print(a)