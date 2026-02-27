students = {101:'Rahul',102:'Raj',103:'Sonam'}

def show(d):
    print(d, type(d))
    print()
    for item in d:
        print(f"{item} : {d[item]}")
show(students)