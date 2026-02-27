# def show():
#     return "This is show function."

# def disp(sh):
#     print("This is disp function.")
#     a = sh()
#     print(a)
# disp(show)



def show():
    return "This is show function."

def disp(sho):
    return f"This is disp function and {sho()}"
a = disp(show)
print(a)