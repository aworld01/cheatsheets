def greater(a,b):
    if a>b:
        return a
    return b




# def greatest(a,b,c):
#     bigger=greater(a,b)
#     return greater(bigger,c)

def greatest(a,b,c):
    return greater(greater(a,b),c)




num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
result=greatest(num1, num2, num3)
print(result)