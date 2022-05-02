"""
A Module is a file containing Python definitions and statements.

A module is a file containing group of variables, methods, functions and classes etc.

They are executed only the first time the module name encountered in an import statement.

The file name is the module name with the suffix .py appended

Type of modules:-
1: User-defined Modules
2: Built-in Modules
	ex: os, sys, math,
	
0:51:00/1:21:21
"""

#import cal
#print("Cal module's variable: ", cal.a)

#cal.name()

#a = cal.add(10, 20)
#print(a)

#b = cal.mul(15, 5)
#print(b)

#mul = cal.mul
#m = mul(5, 6)
#print(m)




#import cal as c
#print("Cal module's variable: ", c.a)

#c.name()

#a = c.add(10, 20)
#print(a)

#b = c.mul(10, 20)
#print(b)

#mul = c.mul
#m = mul(20, 15)
#print(m)



#from cal import a, name, add as ad, mul
#print(a)

#name()

#a = mul(5, 7)
#print(a)

#b = ad(4, 2)
#print(b)



#from cal import*
#print(a)

#name()

#b = add(3, 8)
#print(b)



#import frst
#import scnd
#b = frst.a
#print(b)
#c = scnd.a
#print(c)



#from frst import name, a
#from scnd import name, a
#print(a)
#name()


#from frst import*
#from scnd import*
#print(a)
#name()






#import fstClass
#c = fstClass.Myclass()
#c.name()
#s = fstClass.Myschool()
#s.show()


#import fstClass as s
#c = s.Myclass()
#c.name()
#s = s.Myschool()
#s.show()


#from fstClass import Myclass, Myschool
#c = Myclass()
#c.name()
#s = Myschool()
#s.show()


#from fstClass import Myclass as c, Myschool as s
#c = c()
#c.name()
#s = s()
#s.show()


#from fstClass import*
#c = Myclass()
#c.name()
#s = Myschool()
#s.show()







#import fstClass
#import sndClass
#c = fstClass.Myclass()
#c.name()
#s = fstClass.Myschool()
#s.show()

#cl = sndClass.Mycollage()
#cl.disp()



#from fstClass import Myclass, Myschool
#from sndClass import Mycollage
#c = Myclass()
#c.name()
#s = Myschool()
#s.show()

#d = Mycollage()
#d.disp()







#import fstClass
#import sndClass
#c = fstClass.Myclass()
#c.name()
#s = fstClass.Myschool()
#s.show()

#d = sndClass.Myclass()
#d.disp()







from fstClass import Myclass, Myschool
c = Myclass()
c.name()
from sndClass import Myclass
c = Myclass()
c.disp()