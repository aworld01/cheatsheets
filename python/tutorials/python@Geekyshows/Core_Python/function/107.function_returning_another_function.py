# def disp():
#     def show():
#         return "This is show function"
#     print("This  is disp function")
#     return show
# r_sh = disp()
# print(r_sh())


def disp(sh):
    print("This is disp function")
    return sh

def show():
    return "This is show function"
r_sh = disp(show)
print(r_sh())