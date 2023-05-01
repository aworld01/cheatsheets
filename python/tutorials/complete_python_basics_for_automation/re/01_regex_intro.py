"""
The regex is a procedure in any language to look for a specified pattern in a given text.
What is a pattern?
    It is a sequence of characters, which represent multiple strings.
The different operations in python re are:
    match()
    search()
    findall()
    finditer()
    sub()
    split()
    compile() and so on.
"""
import re

string = "python is simple and it is a very easy language."
new = re.split("i[st]", string)
print(new)