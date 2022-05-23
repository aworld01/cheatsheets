list1=[1,2,5,8]
list2=[1,2,7,6]

def common(l1,l2):
    result=[]
    for i in l1:
        if i in l2:
            result.append(i)
    return result
print(common(list1, list2))