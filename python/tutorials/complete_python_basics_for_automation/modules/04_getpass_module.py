"""
getpass(): prompts the user for a password without echoing. The getpass() module provides a secure way to handle the password prompts where programs interact with the users via the terminal.

getuser(): function displays the login name of the user. This function checks the environment variables LOGNAME, USER, LNAME and USERNAME, in ourder, and returns the value of the first non-empty string.

#!/usr/local/bin/python3
"""

import getpass as gp

"""example1"""
# password = gp.getpass() #to hide password (by default prompt="Password")
# print(f"You have entered: {password}")


"""example2"""
# password = gp.getpass(prompt="Enter your password: ") #prompt="Enter your password: " (changed prompt)
# print(f"You have entered: {password}")


"""example3"""
user = gp.getuser() #to get logged in user name
print(f"Your user name is: {user}")