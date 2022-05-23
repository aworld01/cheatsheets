"""method-1"""
# def is_palindrom(word):
#     reversed_word=word[::-1]
#     if word==reversed_word:
#         return "Palindrom word"
#     else:
#         return "Not Palindrom"

# print(is_palindrom("naman"))
# print(is_palindrom("horse"))


"""method-2"""
# def is_palindrom(word):
#     if word==word[::-1]:
#         return "Palindrom word"
#     return "Not Palindrom"

# print(is_palindrom("naman"))
# print(is_palindrom("horse"))


"""method-3"""
def is_palindrom(word):
    return word==word[::-1]

print(is_palindrom("naman"))
print(is_palindrom("horse"))