"""
print(bool(empty_list)) #False
print(bool(none-empty_list)) #True

06:00 / 28:27
"""

"""defining list"""
l1 = [] #empty list
l2 = [3,2,4,"python",5,6] #list with values (any datatype)

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
print(l1)
print(l2)
print(type(l2))
print(l2[3]) #access python (by index)
print(l2[-2]) #access 5 (by negative index)

