import re

"""check email ids"""
# with open("test.txt", "r") as rf:
#     s = rf.read()

# def getEmails(s):
#     pattern = re.compile(r"(\D\w+@\w+)(.com|.in|.co.in|.co.uk)")
#     match = pattern.findall(s)
#     if match:
#         return match
#     else:
#         return None

# emails = getEmails(s)
# if emails:
#     for email in emails:
#         print(f"{email[0]}{email[1]}")


"""check marble characters"""
s = "BatMan, SuperMan, WonderWoman, Hulk, IronMan, Junierji, Shaktimaan, Thor"

def findMarvel(s):
    pattern = re.compile(r"IronMan|Hulk|Thor")
    match = pattern.findall(s)
    if match:
        return match
    else:
        return None

print(findMarvel(s))