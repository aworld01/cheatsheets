import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
print(percentage) #original format
print()
percentage=float(f'{percentage:.1f}') #modified format

per=f"sir our system have {percentage} percent battery"

print(per)