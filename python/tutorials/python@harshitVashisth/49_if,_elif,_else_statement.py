age=int(input("Enter your age: "))

if age == 0 or age < 0:
    print("\tPlease type a valid number....")
elif 0 < age <= 3:
    print("\tTicket price: Free")
elif 3 < age <= 10:
    print("\tTicket price: Rs.150")
elif 10 < age <= 60:
    print("\tTicket price: Rs.250")
else:
    print("\tTicket price: Rs.200")