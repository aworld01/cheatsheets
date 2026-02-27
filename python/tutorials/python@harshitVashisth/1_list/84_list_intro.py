"""
List is a data_structure that can hold any type of data.
List is a ordered collection of items.
we create our list using square brackets [].
you can store anything in list: int, float, string etc
"""

"""defining list"""
# numbers=[1, 2, 3, 4]
# print(numbers)

# words=["word1", "word2", "word3", "word4"]
# print(words)

# mixed=[1, 2, 1.5, 2.3, "one", "two", None]
# print(mixed)

"""to access list items"""
# numbers=[1, 2, 3, 4]
# num1=numbers[0]
# num2=numbers[2]
# print(num1)
# print(num2)

"""slicing list items"""
# numbers=[1, 2, 3, 4]
# num=numbers[:2]
# print(num)

# words=["word1", "word2", "word3", "word4"]
# wd=words[:2]
# print(wd)

# words=["word1", "word2", "word3", "word4"]
# wd=words[-1]
# print(wd)

"""change list data"""
"""example-1"""
# words=["word1", "word2", "word3", "word4"]
# print(words)
# words[2]="Apple" #to change list data
# print(words)

"""example-2"""
# words=["word1", "word2", "word3", "word4"]
# print(words)
# words[2:]="Apple" #to store as string
# print(words)

"""example-3"""
# words=["word1", "word2", "word3", "word4"]
# print(words)
# words[2:]=["Apple"]
# print(words)

"""example-4"""
words=["word1", "word2", "word3", "word4"]
print(words)
words[2:]=["Apple", "Mango"]
print(words)