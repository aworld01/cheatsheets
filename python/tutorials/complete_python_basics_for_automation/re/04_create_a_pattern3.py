import re

# txt = "This is a pythonnnn and python aaa haaafd aaaaaaaa"

"""example1"""
# pattern = r"\bpythonnnn\b" #to get n numbers of python word
# print(re.findall(pattern, txt))

"""example2"""
# pattern = r"\bpython{4}\b" #to get n numbers of python word
# print(re.findall(pattern, txt))

"""example3"""
# pattern = r"\ba{3}\b" #to get n numbers of a word
# print(re.findall(pattern, txt))




txt = "xaz asdfa sdf xaazz xaaaaaaaaz xaaaaz"

"""2, 3 or 4 times"""
# pattern = r"\bxa{1,4}z\b"
# print(re.findall(pattern, txt))



txt = "xz xaz asdfa sdf xaazz xaaaaaaaaz xaaaaz"

"""two or more times"""
# pattern = r"\bxa{2,}z\b"
# print(re.findall(pattern, txt))

"""one or more times"""
# pattern = r"\bxa{1,}z\b"
# print(re.findall(pattern, txt))


"""one or more times with +"""
# pattern = r"\bxa+z\b"
# print(re.findall(pattern, txt))


"""zero or more times with *"""
# pattern = r"\bxa*z\b"
# print(re.findall(pattern, txt))


"""?: once or none (lazy)"""
pattern = r"\bxa?z\b"
print(re.findall(pattern, txt))