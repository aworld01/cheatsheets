users = ['Rohan Das', 'Shubham', 'Mahimudul Hussain']
computers = ['Raspberry PI-4', 'Android', 'iphone6']

# for i in range (len(users)):
#     print('Computer used by', users[i], 'is:', computers[i])


## with format function (exmp-1)
# for i in range(len(users)):
#     templete = 'Computer used by {} is {}.'
#     data = templete.format(users[i], computers[i])
#     print(data)


## with format function (exmp-2)
for i in range(len(users)):
    templete = 'Computer used by {1} is {0}.'
    data = templete.format(users[i], computers[i])
    print(data)