import random

"""
random(): This generates floating value between 0 and 1 (including 0 but excluding 1).
It doesn't require any argument.
"""
# n=random.random()
# print(n)


"""
randrange(): This method always returns an integer between given lower and upper limit to this method (excluding upper limit)
E.g:
random.randrange(20) will return integers between 0 to 19.
random.randrange(2,8,2) will generate any random number from the value 2,4,6 (step value is 2)
Syntax:
random.randrange(lower_limit, upper_limit, stepvalue)
"""
# n=random.randrange(20)
# print(n)

# n=random.randrange(2,6)
# print(n)

# n=random.randrange(2,8,2)
# print(n)

# n=random.randrange(6,2,-1)
# print(n)


"""
randint(): This method takes 2 parameters a,b in which first one is lower and second is upper limit.
This function returns any integer number between the two numbers, including both limits.
Syntax:
random.randint(a,b) It will generate random integer values within the range a to b (including a and b both), where a must be <= b.
Ex:
random.randint(3,7) will generate randomly integer values between 3 and 7. (both boundary values will be included)
"""
# n=random.randint(3,5)
# print(n)


"""
uniform(): This method returns any floating-point number between two given numbers.
Get a random number in the range (a,b) or (a,b) depending on rounding.

help(random.uniform): to get help about uniform function
"""
# print(help(random))

# print(help(random.uniform))

# n=random.uniform(2,4)
# print(n)


"""
choice(): This method is used for random selection from list, tuple or string or any other sequence.
Returns a random element from the given sequence.
"""
# l=[11,22,33,44,50]
# r=random.choice(l)
# print(r)