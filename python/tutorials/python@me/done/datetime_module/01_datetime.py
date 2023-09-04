from datetime import datetime

"""example1"""
# now = datetime.now()
# print(now)
# print()

# print(f"{now.day}/{now.month}/{now.year}") #4/9/2023
# print(f"{now.hour}:{now.minute}:{now.second}") #3:46:37


"""example2 (order matters)"""
today1 = datetime(2012,6,15) #year,month,day
today2 = datetime(2012,6,15,14,43,53) #year,month,day,hour,minute,second
print(today1)
print(today2)
print()


"""order doesn't matters"""
today1 = datetime(day=30,month=5,year=2013)
today2 = datetime(day=30,month=5,year=2013,hour=14,minute=12,second=45)
print(today1)
print(today2)
print()

print(today2.year)
print(today2.month)
print(today2.day)
print(today2.hour)
print(today2.minute)
print(today2.second)