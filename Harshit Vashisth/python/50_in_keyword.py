name=input("Enter your name please: ")
check=input("Enter a charecter to check: ")

if check in name:
    print("\t", check, "is present in name...")
else:
    print("\t", check, "is not present in name....")