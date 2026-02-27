"""
* = 0,1,2-N
+ = 1,2,3-N
\b = starts with
^ = startswith
[^] = except
$ = endswith
. = any character
\s = space
\w: a-z,A-z,0-9,_
r": ignore escape sequence


re Functions
============
1 => findall: returns a list containing all matches.
2 => search: returns a match object if there is a match anywhare in the string.
3 => split: returns a list where the string has been split each match.
4 => sub: replaces one or many matches with a string.

Metacharacters: Characters with a special meaning.
"""

import re
txt = "The rain in Spain"
p = re.findall("^The.*Spain",txt)
print(p)
print()

"""1. Find all lower case characters alphabetically between 'a' and 'm':"""
txt = "The rain in Spain"
p = re.findall("[a-m]",txt) #a set of characters
print(p)
print()

"""2. Find all digit characters"""
txt = "That will be 59 dollars"
p = re.findall("\d",txt)
print(p)
print()

"""3. Search for a sequence start with 'he', followed by two characters then 'o'"""
txt = "I am saying hello world"
p = re.findall("he..o",txt) #any character (except newline character)
print(p)
print()

"""4. Check if the string ends with 'world'"""
txt = "Hello world"
p = re.findall("world$",txt)
print(p)
print()

"""5. Check if the string contains 'ai' followed by 0 or more 'x' characters"""
txt = "The rain in Spain falls mainly in the plain!"
p = re.findall("aix*",txt)
print(p)
print()

"""6. Check if the string contains 'ai' followed by 1 or more 'x' characters"""
txt = "The rain in Spain falls mainly in the plain!"
p = re.findall("aix+",txt)
print(p)
print()

"""7. Check if the string contains 'a' followed by exactly two 'l' characters"""
txt = "The rain in Spain falls mainly in the plain!"
p = re.findall("al{2}",txt)
print(p)
print()

"""8. Check if the string contains either 'falls' or 'stays'"""
txt = "The rain in Spain falls mainly in the plain!"
p = re.findall("falls|stays",txt)
print(p)
print()

"""9. Return a match at every white-space character"""
txt = "The rain in Spain falls mainly in the plain!"
p = re.findall("\s",txt)
print(p)
print()

"""10. Return a match at every character: from a to z, 0 to 9, and the underscore _ character"""
txt = "The rain in Spain"
p = re.findall("\w",txt)
print(p)
print()

"""11. Check if the string has any a,r, or n character"""
txt = "The rain in Spain"
p = re.findall("[arn]",txt)
print(p)
print()

"""12. Check if the string has any characters between a and n"""
txt = "The rain in Spain"
p = re.findall("[a-n]",txt)
print(p)
print()

"""13. Check if the string has other characters then a, r, and n"""
txt = "The rain in Spain"
p = re.findall("[^arn]",txt)
print(p)
print()

"""14. Check if the string has any 0,1,2, or 3 digits"""
txt = "The rain in Spain 34"
p = re.findall("[^0123]",txt)
print(p)
print()

"""15. Check if the string has any digit"""
txt = "8 times before 11:45 AM"
# p = re.findall("[0-9]",txt)
p = re.findall("\d",txt)
print(p)
print()

"""16. Check if the string has any two-digit numbers, from 00 to 59"""
txt = "8 times before 11:45 AM"
p = re.findall("[0-5][0-9]",txt)
print(p)
print()

"""17. Check if the string has any characters from 'a' to 'z' lower case, and 'A' to 'Z' upper case"""
txt = "8 times before 11:45 AM"
p = re.findall("[a-zA-Z]",txt)
print(p)
print()





"""The search() function: Searches the string and returns a Match object if there is match. If there is more than one match, only the first occurrence of the match will be returned."""
"""1. Search for the first white-space character in the string"""
txt = "The rain in Spain"
p = re.search("\s", txt)
print(p)
print()

"""2. If no matches are found, the value None is returned"""
txt = "The rain in Spain"
p = re.search("\d", txt)
print(p)
print()



"""The split() function: Returns a list where the string has been split at each match."""
"""Split the string at every white-space character"""
txt = "The rain in Spain"
p = re.split("\s",txt)
print(p)
print()

"""Split the string at only first white-space occurence"""
txt = "The rain in Spain"
# p = re.split("\s",txt,maxsplit=1)
p = re.split("\s",txt,1)
print(p)
print()


"""The sub() function: Replaces the matches with the text of your choice"""
"""1. Replace every white-space character with _"""
txt = "The rain in Spain"
p = re.sub("\s","_",txt)
print(p)

"""2. Replace the first two occurrences of a white-space character with _"""
txt = "The rain in Spain"
p = re.sub("\s","_",txt,2)
print(p)
print()

"""
Match Object: Object containing information about the search and the result. If there is no match, the value None will be returned, instead of the Match Object.
"""
txt = "The rain in Spain"
p = re.search("ai",txt)
print(p)
print()


"""
The Match object has methods used to retrieve information about the search, and the result:-
    .span(): returns a tuple containing the start & end position of the match.
    .string(): returns the string passed into the function.
    .group() returns the part of the string where there was a match.

"""
txt = "The rain in Spain"
p = re.search(r"\bS\w+",txt)
print(p)
print(p.string)
print(p.group())
print(p.span())
print(p.start())
print(p.end())