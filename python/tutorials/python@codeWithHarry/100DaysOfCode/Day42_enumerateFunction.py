marks = [12, 58, 42, 89, 13, 45, 1, 4]

"""example1"""
# index = 0
# for mark in marks:
#     index += 1
#     print(f"{index} => {mark}")
#     if (index == 3):
#         print("You are awesome!")


"""example2"""
# for mark in enumerate(marks):
#     print(mark)


"""example2"""
# for index, mark in enumerate(marks):
#     print(f"{index} => {mark}")


"""example3"""
# for index, mark in enumerate(marks, start=1):
#     print(f"{index} => {mark}")


"""example4"""
for index, mark in enumerate(marks):
    print(f"{index} => {mark}")
    if (index == 3):
        print("You are awesome")