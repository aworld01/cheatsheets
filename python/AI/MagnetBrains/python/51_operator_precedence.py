"""example1"""
print(6-3*4) #3*4=12, 6-12=-6

"""example2"""
print((6-3)*4) #6-3=3, 3*4=12

"""example3"""
x,y = "science",0
print(x=="science" or x=="maths" and y>=2) #True

"""example4"""
x,y = "python", "java"
print((x=="python" or x=="c++") and y=="SQL") #False

"""example5"""
print(6*3//10) #6*3=18, 18//10=1

"""example6"""
print(7/2*6%4) #7/2=3.5, 3.5*6=21, 21%4=1.0

"""example7"""
print(2**4**2) #4**2=16, 16**2=65536

"""example8"""
a = 10
a+=100+200/10-3*10 #200/10=20, 20-30=-10, -10+100=90, 90+10=100.0
print(a)