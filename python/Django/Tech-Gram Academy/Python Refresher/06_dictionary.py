dic={"name":"Abdul Zoha", "age":28, "email":"abdulzoha786@gmail.com"}
# print(dic)

# print(dic["email"])

# del dic["age"] #to delete dictionary iteme.
# print(dic)

# print(len(dic)) #to get dictionary length.

##to print keys of dictionary
# for key in dic:
#     print(key)



##to print keys and values of dictionary.
for key in dic.items():
    print(key)
print()

for key, value in dic.items():
    print(key,"=", value)