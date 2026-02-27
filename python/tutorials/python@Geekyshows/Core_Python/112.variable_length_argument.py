def add(*num):
    z = num[0] + num[1] + num[2]
    return z
a = add(30,40,50)
print(a)


def add(x, *num):
    z = x + num[0] + num[1]
    return z
a = add(30,40,50)
print(a)