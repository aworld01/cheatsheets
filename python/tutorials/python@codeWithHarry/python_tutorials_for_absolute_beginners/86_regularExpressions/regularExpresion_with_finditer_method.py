"""
findall, search, split, sub, finditer

Meta Characters
---------------
[]: A set of characters.
\: Signals a specialSequence (can also be used to escape special characters).
.: Any character (except newline character).
^: Starts with.
$: Ends with.
*: Zero or more occurrences.
+: One or more occurrences.
{}: Exactly the specified number of occurrences.
(): Capture and group.

Special Sequences
-----------------
\A: Returns a match if the specified characters are at the beginning of the string.
\b: Returns a match where the specified characters are at the beginning or at the end of a word.
\B: Returns a match where the specified characters are present, but not at the beginning or at the end of a word.
\d: Returns a match where the string contains digits (number from 0-9).
\D: Returns a match where the string doesn't contain digits.
\s: Returns a match where the string contains a white space character.
\S: Returns a match where the string doesn't contain a white space character.
\w: Returns a match where the string contains any word characters (characters from a-z, digits from 0-9 and the underscore _ character).
\W: Returns a match where the string doesn't contain any word characters.
\Z: Returns a match if the specified characters are at the end of the string.
"""

def string():
    with open("test.txt", "r") as rf:
        data = rf.read()
        return data

data = string()

import re

"""example-1"""
# pattern = re.compile(r"fass")
# matchs = pattern.finditer(data)
# for match in matchs: #returns position, Result in object form.
#     print(match)

# data = data[448: 452]
# print(data)


"""example-2"""
# pattern = re.compile(r".adm") #any character (except newline character)
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-3"""
# pattern = re.compile(r"^Tata") #starts with
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-4"""
# pattern = re.compile(r"iin$") #ends with
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-5"""
# pattern = re.compile(r"ai*") #Zero or more occurrences.
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-6"""
# pattern = re.compile(r"ai+") #one or more occurrences.
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-6"""
# pattern = re.compile(r"ai{2}") #Exactly the specified number of occurrences.
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-7"""
# pattern = re.compile(r"ai{1}|tata") #Either or.
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-8"""
# pattern = re.compile(r"\ATata") #Either or.
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-9"""
# pattern = re.compile(r"\btata")
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-10"""
# pattern = re.compile(r"tata\b")
# matchs = pattern.finditer(data)
# for match in matchs:
#     print(match)


"""example-11"""
pattern = re.compile(r"\d{5}-\d{4}")
matchs = pattern.finditer(data)
for match in matchs:
    print(match)