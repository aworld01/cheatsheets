def add(**num):
    z = num['a'] + num['b'] + num['c']
    return z
a = add(a=5,b=4,c=5)
print(a)


def add(x, **num):
    z = x + num['a'] + num['c']
    return z
a = add(30,a=4,b=5,c=7)
print(a)