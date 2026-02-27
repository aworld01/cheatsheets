"""
DictReader(f) #Default delimiter is comma(",")
DictReader(f, delimiter='=') #if delimiter is colan(":")
You can use delimiter with reader and DictReader
"""

from csv import DictReader

"""example-1"""
# with open('file.csv', 'r') as f:
#     csv = DictReader(f) #ordered dict
#     for row in csv:
#         print(row)


"""example-2"""
with open('file.csv', 'r') as f:
    csv = DictReader(f)
    for row in csv:
        print(row["email"])


"""delimiter colan"""
with open('file2.csv', 'r') as f:
    csv = DictReader(f, delimiter=":")
    for row in csv:
        print(row)