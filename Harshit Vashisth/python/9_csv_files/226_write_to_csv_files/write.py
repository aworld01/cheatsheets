"""
There are two ways to write csv files:-
1: writer, DictWriter

There are two methods:-
writerow: to write a single row
writerows: to write multiple rows
newline='': to remove linespace
"""
"""writerow"""
# from csv import writer
# with open('file.csv', 'w', newline='') as f:
#     csv = writer(f)
#     csv.writerow(["name", "country", "phone"])



"""writerows"""
from csv import writer
with open('file.csv', 'w', newline='') as f:
    csv = writer(f)
    csv.writerows([["name", "country", "phone"],["Abdul Zoha", "India",+919006228083]])