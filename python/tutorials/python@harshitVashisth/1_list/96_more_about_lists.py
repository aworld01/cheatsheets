"""generate lists with range function"""
# numbers=list(range(1,11))
# print(numbers)

"""something more about pop() method"""
# num=numbers.pop()
# print(numbers)
# print(f"Poped item is: {num}")

 

"""index method()"""
"""Example-1"""
# numbers=[1,2,3,4,5,6,7,8,9,1]
# index=numbers.index(1) #to get first index position
# print(index)
# index2=numbers.index(1, index+1) #to get next index position
# print(index2)

"""Example-2"""
# string="Hello world"
# find=string.index("w")
# print(find)


"""pass list to a function"""
numbers=list(range(1,11))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))