from datetime import datetime

time=datetime.now()
time2=time.strftime("%H:%M:%S")
time3=time.strftime("%H")

hour=time.hour
minute=time.minute

print(time2,type(time2))
print(time3,type(time3))
print(minute,type(minute))