# def disp():
#     def show():
#         print("This is show function")
#     print("This is disp function")
#     show()
# disp()


# def disp():
#     def show():
#         return "This is show function"
#     result = f"{show()} This is disp function"
#     return result
# a = disp()
# print(a)


def disp(st):
    def show():
        return "This is show function"
    result = f"{st} {show()} This is disp function"
    return result
a = disp("Hello world!")
print(a)