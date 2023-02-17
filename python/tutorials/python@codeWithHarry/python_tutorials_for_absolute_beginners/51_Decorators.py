# def func1():
#     print("Subscribe now")

# func2 = func1 #to make another copy
# del func1 #to delete func1

# func2() #to call func2



"""example-1"""
"""Creating decorator"""
# def dec1(arg):
#     def func1():
#         print("Executing now")
#         arg()
#         print("Executed")
#     return func1

# def func2():
#     print("Hello Abdul Zoha")

# func2 = dec1(func2) #calling decorator
# func2() #calling function


"""example-2"""
"""Creating decorator"""
def dec1(arg):
    def func1():
        print("Executing now...")
        arg()
        print("Executed...")
    return func1

@dec1 #calling decorator
def func2():
    print("Hello Abdul Zoha sir...")

func2() #calling function