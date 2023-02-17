from re import T


students = {101:'Rahul',102:'Raj',103:'Sonam'}

def show(d):
    t = d, type(d)
    return t
s = show(students)
print(s)