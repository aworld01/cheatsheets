"""
0 1 1 2 3 5 8 13 21 34

1: 0
2: 0 1
3: 0 1 1
"""
# for i in range(1, 11):
#     print(i, end="\n") #\n" is default.

# for i in range(1, 11):
#     print(i, end=" ")

# for i in range(1, 11):
#     print(i, end=", ")




def fibonacci_seq(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c=a+b #c=1,2,3
            a=b
            b=c
            print(b, end=" ")

num=int(input("Enter the number: "))
fibonacci_seq(num)