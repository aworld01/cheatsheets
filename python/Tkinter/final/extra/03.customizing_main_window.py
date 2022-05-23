from tkinter import*
root = Tk()
root.title("Home")
root.config(bg="green")

'''
root.geometry('widthxheight+x+y')

#TO PUT WINDOW ON CENTER
w = 800
h = 800
#to findout window size:
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

#TO PUT WINDOW ON CENTER
x = int(ws/2 - w/2) #to get center point of width (default may be float so use int())
y = int(hs/2 - h/2) #to get center point of height

data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)


#########################################################################################
#TO PUT WINDOW ON CENTER
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws/2 - w/2) #to get center point of width (default may be float so use int())
y = int(hs/2 - h/2) #to get center point of height
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

#TO PUT RIGHT-TOP
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws-w)
y = 0
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

TO PUT RIGHT-BOTTOM
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws-w)
y = int(hs-h)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

TO PUT LEFT-TOP
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = 0
y = 0
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

TO PUT LEFT-BOTTOM
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = 0
y = int(hs-h)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

TOP-CENTER
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws/2 - w/2)
y = 0
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

BOTTOM-CENTER
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws/2 - w/2)
y = int(hs - h)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

LEFT-CENTER
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = 0
y = int(hs/2 - h/2)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

RIGHT-CENTER
w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws-w)
y = int(hs/2 - h/2)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)
'''

w = 800
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws/2 - w/2)
y = int(hs - h)
data = str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

root.mainloop()

#09:30/15:57