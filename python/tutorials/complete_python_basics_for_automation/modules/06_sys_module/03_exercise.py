import sys

if len(sys.argv) < 3:
    sys.exit()

"""taking arguments"""
usrStr = sys.argv[1]
usrAction =sys.argv[2]

"""appling logics"""
if usrAction == "lower":
    print(usrStr.lower())
elif usrAction == "upper":
    print(usrStr.upper())
elif usrAction == "title":
    print(usrStr.title())
elif usrAction == "capitalize":
    print(usrStr.capitalize())
elif usrAction == "swapcase":
    print(usrStr.swapcase())
else:
    print("Your input is not valid. Pleas select valid option from this List: lower/upper/title/capitalize/swapcase")