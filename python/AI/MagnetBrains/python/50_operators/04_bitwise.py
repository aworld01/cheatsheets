a = 9 #1001
b = 10 #1010

print(bin(a))
print(bin(b))

"""and"""
print(f"{a&b} => {bin(a&b)}")

"""or"""
print(f"{a|b} => {bin(a|b)}")

"""not"""
print(f"{~b} => {bin(~b)}")

"""xor"""
print(f"{a^b} => {bin(a^b)}")

"""right shift"""
print(f"{b>>2} => {bin(b>>2)}")

"""left shift"""
print(f"{b<<2} => {bin(b<<2)}")