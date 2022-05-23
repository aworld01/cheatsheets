import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
percentage=float(f'{percentage:.1f}')

per=f"Sir our system have {percentage} percent battery"
print(per, end=', ')

if percentage>=75:
    print(per, 'We have enough power to continue our work')
elif percentage>=40 and percentage<=75:
    print('We should connect our system to charging point to charge our battery')
elif percentage>=15 and percentage<=30:
    print("We don't have enough power to work, please connect to charging")
elif percentage<=15:
    print("we have very low power, please connect to charging the system will shutdown very soon")