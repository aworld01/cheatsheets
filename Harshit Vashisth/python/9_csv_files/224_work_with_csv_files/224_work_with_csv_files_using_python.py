from csv import reader
"""example-1"""
# with open('file.csv', 'r') as f:
#     csv = reader(f) # csv is an iterator
#     # print(csv, type(csv))
#     for row in csv:
#         print(row)


with open('file.csv', 'r') as f:
    csv = reader(f)
    next(csv) #to skip first line
    for row in csv:
        print(row)