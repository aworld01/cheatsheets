## Method-1
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# avr=(f"{(a+b+c)/3}")
# print(f"Average is: {avr}")

## Method-2
a, b, c=input("Enter any three numbers separated by comma: ").split(",")
avr=(f"{(int(a)+int(b)+int(c))/3}")
print(f"Average is: {avr}")