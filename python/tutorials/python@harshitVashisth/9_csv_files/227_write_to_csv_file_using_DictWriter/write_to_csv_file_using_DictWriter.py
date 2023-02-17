"""
reader
writer
DictReader
DictWriter

writerow
writerows
"""

from csv import DictWriter

# with open('Person.csv', 'w',newline='') as f:
#     csv = DictWriter(f, fieldnames=["name", "age", "contact"]) #to spacify header
#     csv.writeheader()

#     """writerow"""
#     csv.writerow({
#         "name": "Abdul Zoha",
#         "age": 29,
#         "contact": +919006228083
#     })
#     csv.writerow({
#         "name": "Abdul Jabbar",
#         "age": 39,
#         "contact": +919006228797
#     })





with open('Person.csv', 'w') as f:
    csv = DictWriter(f, fieldnames=["name", "age", "contact"]) #to spacify header
    csv.writeheader()
    
    """writerows"""
    csv.writerows([
        {"name": "Abdul Zoha","age": 29,"contact": +919006228083},
        {"name": "Aftab Alam","age": 25,"contact": +919006276589},
        {"name": "Zafar","age": 31,"contact": +919006285634}
    ])
