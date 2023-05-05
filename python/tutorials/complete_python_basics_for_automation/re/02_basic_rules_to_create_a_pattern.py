"""
re is the module to perform regex in Python. (use import re in scripts)
There are different operations in re like:
    search, match, finditer, findall, split, sub etc...

syntax:
    re.search(pattern, text)
    re.match(pattern, text)
    re.finditer(pattern, text)
    re.findall(pattern, text)

Pattern is a sequence of characters, which represent multiple strings.
Simple examples for pattern:
    "Python"
    "Python"[23] => "Python2" "Python3"

Rules to create a pattern:
    a, x, 9 => Ordinary characters that match themselves
    [abc] =>   Matches a, b, or c
    [a-c] =>   Matches a, b, or c (sequence of characters)
    [a-zA-Z0-9] =>  Matches any letter from (a to z) or (A to Z) or (0 to 9)
    \w => Matches any single letter, digit or underscore
    \W => Matches any character not part of \w
    \d => Matches decimal digit 0-9
    . => Matches any single character except newline character
"""
import re

"""pattern creation with findall operation"""
"""example1"""
# print(re.findall("is","This is python and it is very easy to learn."))


"""example2"""
# txt = "This is python and it is very easy to learn."
# myPattern = "is"
# result = re.findall(myPattern, txt) #to find result
# n = len(result) #to find length of result
# print(result)
# print(n)


"""find either a,b or v"""
# txt = "This is python and it is very easy to learn."
# myPattern = "[abv]"
# result = re.findall(myPattern, txt) #to find result
# n = len(result) #to find length of result
# print(result)
# print(n)


"""findout sequence of characters"""
# txt = "hidkl abd xyz"
# myPattern = "[a-d x-z j h-l]"
# result = re.findall(myPattern, txt) #to find result
# n = len(result) #to find length of result
# print(result)
# print(n)


"""findout either is or it"""
# txt = "This is python and it 412346 is very easy to learn."
# myPattern = "i[st]"
# result = re.findall(myPattern, txt) #to find result
# n = len(result) #to find length of result
# print(result)
# print(n)


"""to remove special characters"""
# # txt = "adl41 2-@_@$&_" #remove special characters example
# txt = "This is python and it 412346 is very easy to learn." #remove spaces example
# myPattern = "\w"
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""Matches any character not part of \w"""
# txt = "This is python and it 412346 is very easy to learn2-@_@$&." #remove spaces example
# myPattern = "\W" #Matches any character not part of \w
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""Matches decimal digit 0-9"""
# txt = "This is python 2 3 4 and it 412346 is very easy to learn2-@_@$&." #remove spaces example
# myPattern = "\d" #Matches decimal digit 0-9
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""Example1"""
# txt = "This is python2 3 4 it @ is easy to _ learn_@ python3" #remove spaces example
# myPattern = "python\d" #Matches decimal digit 0-9
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""Example2"""
# txt = "This is python2 34 it @ is easy to _ learn_@ python3" #remove spaces example
# myPattern = "\d\d" #Matches decimal digit 0-9
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""select all except newline character"""
# txt = "This is python2 34 it @ is easy to _ learn_@ \n python3" #remove spaces example
# myPattern = "." #Matches decimal digit 0-9
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""select dot"""
# txt = "This is python2 34 it @ is easy. to _ learn_@ \n python3." #remove spaces example
# myPattern = "\." #Matches decimal digit 0-9
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""example of dot"""
# txt = "This is my ip of a db server: 255.100.102.103  338339339383839393776678" #remove spaces example
# myPattern = "\d\d\d.\d\d\d.\d\d\d" #Matches decimal digit 0-9
# result = re.findall(myPattern, txt)
# n = len(result)
# print(result)
# print(n)


"""final example of dot"""
txt = "This is my ip of a db server: 255.100.102.103  338339339383839393776678" #remove spaces example
myPattern = "\d\d\d\.\d\d\d\.\d\d\d" #Matches decimal digit 0-9
result = re.findall(myPattern, txt)
n = len(result)
print(result)
print(n)