import psutil

battery=psutil.sensors_battery()
percentage=battery.percent
percentage=float(f'{percentage:.1f}')
per=f"\tSir our system have {percentage} percent battery"

data={
    "hi":"hello sir!",
    "hello":"hi sir!",
    "how are you?":"I'm fine sir",
    "who are you?":"I'm a computer program, my name is Alexa",
    "what is your name?":"My name is Alexa, please tell me how may I help you?",
    "how old are you?":"I'm 18 years old now sir!",
    "goodbye alexa":"Shutting down, thank you sir!"
}
while True:
    d=input('Ask you question: ').lower()

    for i in data:
        q=i
        a=data[i]

        if d in q:
            print('\t',a)
    
    if d in 'how much battary do we have?':
        print(per, end=', ')
        if percentage>=75:
            print('We have enough power to continue our work')
        elif percentage>=40 and percentage<=75:
            print('We should connect our system to charging point')
        elif percentage>=15 and percentage<=30:
            print("We don't have enough power to work, please connect to charging")
        elif percentage<=15:
            print("we have very low power, please connect to charging the system will shutdown very soon")
    elif d in q:
        break
        print('\t',a)