'''
Formatted String Literals
'''

# print("**********Integer**********")
# a = 10
# b = 20
# print(f"{a}")
# print(f"{a} {b}")
# print()
# print()

# print("**********Float**********")
# c = 10.56
# d = 20.42
# print(f"{c}")
# print(f"{c} {d}")
# print(f"{d}  {c}")
# print()
# print()

# print("**********String**********")
# f_name = "Abdul"
# l_name = "Zoha"
# print(f"{f_name}")
# print(f"{f_name} {l_name}")
# print(f"{l_name} {f_name}")


# print("**********String_and_Integer**********")
# name = "Abdul Zoha"
# age = 26
# print(f"Hello {name}, your age is {age}.")



# print("**********Integer**********")
# num = 15
# print(f"{num}")
# print(f"{num:d}")
# print(f"{num:6d}")
# print(f"{num:06d}")
# print(f"{num:+6d}")
# print(f"{num:<6d}")
# print(f"{num:*<6d}")
# print(f"{num:*>6d}")
# print(f"{num:^6d}")
# print(f"{num:*^6d}")


# print("**********Float**********")
# num = 15.65
# price = 15.65123456789
# print(f"{num}")
# print(f"{num:f}")
# print(f"{num:8f}")
# print(f"{price:.20f}")
# print(f"{num:8.3f}")
# print(f"{num:+8.2f}")
# print(f"{num:<8.2f}")
# print(f"{num:*<8.2f}")
# print(f"{num:*>8.2f}")
# print(f"{num:^8.2f}")
# print(f"{num:*^8.2f}")


# print("**********String**********")
# name = "Abdul"
# print(f"{name}")
# print(f"{name:s}")
# print(f"{name:8s}")
# print(f"{name:<8}")
# print(f"{name:*<8}")
# print(f"{name:>8}")
# print(f"{name:*>8s}")
# print(f"{name:^8s}")
# print(f"{name:*^8s}")


# print("**********Truncating_String**********")
# name = "Abdul"
# print(f"{name:.3s}")
# print(f"{name:8.3s}")
# print(f"{name:*<8.3s}")
# print(f"{name:>8.3s}")
# print(f"{name:*>8.3s}")
# print(f"{name:^8.3s}")
# print(f"{name:*^8.3s}")


# price = 123456789
# print(f"{price:,}") #thousand seperator
# print(f"{price:_}") #thousand seperator

# print(f"{10*8}")

# a = 50
# b = 3
# print(f"{a/b}")

# a = 50
# b = 3
# print(f"{a/b:.2}")

# a = 50
# b = 3
# print(f"{a/b:.2%}")

# value = (10,20,30)
# print(f"{value[0]}")
# print(f"{value[2]}")



# data = {'Rahul':2000, 'Sonam':3000}
# print(f"{data['Rahul']} {data['Sonam']}")
# print()
# data = {'Rahul':2000, 'Sonam':3000}
# print(f"Rahul's salary is: {data['Rahul']}.")
# print(f"Sonam's salary is: {data['Sonam']}.")


# s = "Hello world!"
# print(f"{s.upper()}")

# print(f"{10}")
# print(f"{{10}}")

from datetime import datetime
today = datetime(2020, 6, 7)
print(f"{today}")
print(f"Today is:{today: %d/%b/%Y}")

