"""
break: to stop infinite loop
"""
# while True:
#     name=input("Enter your name: ")
#     if name == "stop":
#         break
#     print(f"\tHi {name}")



"""
continue: to skip anything
"""
for i in range(1,11):
    if i==6:
        continue
    print(f"{i} Hello world!")