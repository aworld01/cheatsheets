'''
strftime() method: This method is used to format the content of datetime, date and time class object. strftime represents string format to time. This method convert the object into a specified format and returns a formatted string.
Ex:-
dt = datetime.today()
ndt = dt.strftime('%B, %d, %Y')
'''

from datetime import datetime
dt = datetime.today()
print(dt)
print()

nd1 = dt.strftime('%B, %d, %Y')
print(nd1)
print()

nd2 = dt.strftime('%d/%b/%Y')
print(nd2)
print()

nd3 = dt.strftime('%d/%m/%Y')
print(nd3)
print()

nd4 = dt.strftime('%H:%M:%S')
print(nd4)
print()