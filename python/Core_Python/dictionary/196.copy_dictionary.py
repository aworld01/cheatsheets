"""
This method is used to copy all the elements from the existing dictionary into a new dictionary.
"""

# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dictionary: ',st)
# print(id(st))
# new_st = st.copy() #to copy dictionary
# print('Copied dictionary: ',new_st)
# print(id(new_st))


st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dictionary: ',st)
print(id(st))
new_st = st.copy() #to copy dictionary
print('Copied dictionary: ',new_st)
print(id(new_st))
st[101] = 'Python'
print('st: ',st)
print('new_st: ',new_st)