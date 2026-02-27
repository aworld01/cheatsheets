import re

s = "Ironwoman is great, I love this character from marvel"

def findMarvel(s):
    pattern = re.compile(r"Iron(wo)?man")
    match = pattern.search(s)
    if match:
        return match.group()
    else:
        return None

print(findMarvel(s))