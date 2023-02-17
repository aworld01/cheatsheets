import re

def getEmails(s):
    pattern = re.compile(r"\D\w+@\w+.\w+")
    match = pattern.findall(s)
    if match:
        return match
    else:
        return None

with open("test.txt", "r") as rf:
    s = rf.read()
    print(getEmails(s))