"""
print(bool(empty_list)) #False
print(bool(none-empty_list)) #True

list method:-
    1: append
    2: clear
    3: copy
    4: count
    5: extend
    6: index
    7: insert
    8: pop
    9: remove
    10: reverse
    11: sort
print(dir(l2)) #to print functions and methods of list


11:00 / 28:27
"""

"""defining list"""
l1 = [] #empty list
l2 = [3,2,4,"python","javaScript",5,6] #list with values (any datatype)

print(l2) #to print list
# print(l1, type(l1)) #to print list and its type

"""
indexing
0 => 3
1 => 2
2 => 4
3 => "python"
4 => 5
5 => 6

indexing by negative values
-1 => 6
-2 => 5
-3 => "python"
-4 => 4
-5 => 2
-6 => 3
"""

"""accessing list values"""
# print(l2[4]) #to find 4th index value
# print(l2[-3]) #from last to 3rd value
# print(l2[4][3]) #to find 'a' form javaScript


"""slicing"""
# print(l2) #no slicing
# print(l2[:]) #from 0 to last
# print(l2[0:]) #from 0 to last
# print(l2[1:]) #from 1 to last
# print(l2[1:4]) #from 1 to 3rd
# print(l2[4][4:10]) #slice 'Script' from javaScript

"""modifying values"""
l2[3] = "Mojo" #to change python into mojo
print(l2)