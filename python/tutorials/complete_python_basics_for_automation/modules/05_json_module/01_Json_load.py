"""
JSON (javaScript Object Notation) is a popular data format used for representing structured data.
"""
import json

file = "testLoad.json"
with open(file, "r") as rf:
    """example1"""
    # data = rf.read() #it will return only string
    # print(data, type(data))

    """example2"""
    data = json.load(rf) #to change data from string to dictionary
    print(data, type(data))