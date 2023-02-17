## input function always takes input in string

#name = input()
#print('Hello', name)

#name = input("What is your name? ") #it will show a message for user.
#print('Hello '+ name)

#name = input('What is your name? ')
#mobile = input('Enter your mobile number: ')
#print('Hello '+name+' your mobile no. is: '+mobile)

#age = input('Enter your age: ')
#t = type(age) #to check datatype
#print(age)
#print(t)

#ag = input('Enter your age: ')
#age1 = type(ag)
#print('Before change: ', age1)
#age = int(ag) #it will change the datatype from str to int.
#age2 = type(age)
#print('After change: ', age2)

age = int(input('Enter your age: ')) #it will automatically change the datatype.
t = type(age)
print(age, t)