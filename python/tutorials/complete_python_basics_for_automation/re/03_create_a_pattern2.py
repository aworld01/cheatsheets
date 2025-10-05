import re

"""example of ^"""
# txt = "it is python and it is easy to learn."
# pattern = "^i[ts]"
# print(re.findall(pattern, txt))

# """example of \\b"""
# txt = "it is python and it is easy to learn learnand."
# pattern = "\\blearn"
# print(re.findall(pattern, txt))

"""example of r"\b"""
# txt = "it is python and it is easy to learn learnand."
# pattern = r"\blearn" #search from joint world too which starts from space.
# print(re.findall(pattern, txt))

"""example of r"\b"""
# txt = "it is python and it is easy to learn learnand."
# pattern = r"\blearn\b" #search a complete word.
# print(re.findall(pattern, txt))

"""example of r"\B"""
# txt = "it is python and it is easy to learn learnand."
# pattern = r"learn\B" #search a pattern from joint word which doesn't ends from space.
# print(re.findall(pattern, txt))

"""example of r"\n"""
# txt = "it is python and it  is easy to  learn \n learnand."
# pattern = r"\n" #search a newline character.
# print(re.findall(pattern, txt))