import re

s = "I have rupees 43"

def findMarvel(s):
    # pattern = re.compile(r"^I have") #start with
    pattern = re.compile(r"\d$") #ends with
    match = pattern.search(s)
    if match:
        return match.group()
    else:
        return None

print(findMarvel(s))