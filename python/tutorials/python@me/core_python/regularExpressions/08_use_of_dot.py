import re

s = "cat mat at bat mate this that in fat rat follow go row .at"

def findMarvel(s):
    # pattern = re.compile(r".at")
    pattern = re.compile(r"\.at")
    match = pattern.findall(s)
    if match:
        return match
    else:
        return None

print(findMarvel(s))