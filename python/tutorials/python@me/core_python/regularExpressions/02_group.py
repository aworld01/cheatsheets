import re

# s = "My mobile number is +919006008083 and my office's number is +919934237649"
# pattern = re.compile(r"(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)")

# match = pattern.search(s)
# f1 = match.group() #to retrieve whole number
# f2 = match.group(1) #to country code
# f3 = match.group(2) #to mobile number

# print(f1, type(f1))
# print(f2, type(f2))
# print(f3, type(f3))





# s = "My mobile number is +919006008083 and my office's number is +919934237649"

# match = re.search(r"(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)", s)
# f1 = match.group(1) #to country code
# f2 = match.group(2) #to mobile number

# print(f"Country code: {f1}")
# print(f"Mobile Number: {f2}")



s = "My mobile number is +919006008083 and my office's number is +919934237649"

def getPhoneNumber(s):
  pattern = re.compile(r"\+\d{12}")
  match = pattern.findall(s)
  if match:
    return match
  else:
    return None

num = getPhoneNumber(s)
print(num)