user_name=input("Enter your name please: ")
user_age=int(input("Enter your age: "))
if user_age>=18 and (user_name[0]=="a" or user_name[0]=="A"):
    print("\tYou can watch coco....")
else:
    print("\tYou can't watch coco....")