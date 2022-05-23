"""example-1"""
# def all_total(*args): #to take n number of arguments in tuple form.
#     print(args, type(args))
# all_total(1, 2, 3, 5, 6)


"""example-2"""
def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total
print(all_total(1,2,3,4,5,6,7,8,9,10))