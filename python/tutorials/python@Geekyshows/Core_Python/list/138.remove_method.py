# # This method is used to remove first occurence of given element from the existing list. If it doesn't found that element, shows ValueError.

a = [10,20,30,40,50,'ArtificialWorld']
print(f"Before remove: {a}")
a.remove('ArtificialWorld')
print(f"After remove: {a}")