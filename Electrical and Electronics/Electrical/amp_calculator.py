"""
Power = Watt
Current = Ampare (I)

R = Resistence (ohm)
W = Watt
I = Current (Ampare)

R = V / I
W = V * I
I = W / V
"""


V = int(input("Enter the voltage: "))
W = int(input("Enter the watts: "))

def electricity(v,w):
    A = w/v
    ohm = v/A
    ohm =  f"{ohm:.2f}"
    I = f"{A:.2f}"
    VA = w/.8
    print()

    print(f"Voltage: {v} V")
    print(f"Watt: {w} W")
    print(f"VA: {VA} VA")
    print(f"Current: {I} A")
    print(f"Resistence: {ohm} Ohm")
    
electricity(V,W)