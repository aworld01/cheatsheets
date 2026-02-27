numbers=list(range(1,11))
print(numbers)

"""Example-1"""
# def reverse_list(num):
#     return num[::-1]
# print(reverse_list(numbers))


"""Example-2"""
# def reverse_list(num):
#     num.reverse()
#     return num
# print(reverse_list(numbers))


"""Example-2"""
def reverse_list(num):
    reverse=[]
    for i in range(len(num)):
        poped_item=num.pop()
        reverse.append(poped_item)
    return reverse
print(reverse_list(numbers))