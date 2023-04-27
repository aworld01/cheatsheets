"""
A string is a sequence of characters and it's imutable.

A character is simply a symbol. For example, the English language has 26 characters.

Computers don't deal with character, the deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0's and 1's.

This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encoding used.

In Python, string is a sequence of Unicode character. Unicode was introduced to include every character in all languages and bring uniformity in encoding.
"""

"""creating a string"""
txt = "" #empty string
txt2 = " " #space is one of the character
firstName = 'Abdul' #string with single quatation
lastName = "Zoha" #string with dauble quatation
info = """I started my carrier as an admin and moved into automation team.
Now I'm 25 years old. And I do my job very easily.
"""

"""printing strings"""
# print(txt)
# print(txt)
# print(firstName)
# print(lastName)
# print(info)

"""deleting string"""
# print(firstName)
# del firstName #to delete a string

"""finding length of a string characters (space is also a character)"""
# print(firstName)
# print(len(firstName))

"""string concatinating"""
print(firstName)
print(f"{firstName} {lastName}")