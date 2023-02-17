from tkinter import*

"""functions"""
def clear():
    ent.delete(0, END)
def inpt(number):
    ent.insert(END, number)
def plus():
    num1 = ent.get()
    global f_num
    f_num = int(num1)
    ent.delete(0, END)
def equal():
    num2 = ent.get()
    ent.delete(0, END)
    ent.insert(END, f_num + int(num2))


root = Tk()
root.title("Simple Calculator")

ent = Entry(root, font=("times", 20, "bold"))

"""define numeric Buttons"""
btn1 = Button(root, text="1", padx=40, pady=20, command=lambda:inpt(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda:inpt(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda:inpt(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda:inpt(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda:inpt(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda:inpt(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda:inpt(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda:inpt(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda:inpt(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda:inpt(0))
btn_dot = Button(root, text=".", padx=43, pady=20, command=inpt)

btn_per = Button(root, text="%", padx=39, pady=20, command=inpt)
btn_plus = Button(root, text="+", padx=40, pady=20, command=plus)
btn_minus = Button(root, text="-", padx=43, pady=20, command=inpt)
btn_multiply = Button(root, text="x", padx=42, pady=20, command=inpt)
btn_divide = Button(root, text="/", padx=44, pady=20, command=inpt)
btn_equal = Button(root, text="=", padx=155, pady=20, command=equal)
btn_clear = Button(root, text="CLEAR", padx=26, pady=20, command=clear)

"""put widgets on the screen"""
ent.grid(row=0, column=0, padx=10, pady=10, ipadx=91, columnspan=4)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn0.grid(row=4, column=0)
btn_dot.grid(row=4, column=1)

btn_per.grid(row=4, column=2)
btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)
btn_equal.grid(row=5, column=0, columnspan=3)
btn_clear.grid(row=5, column=3)

root.mainloop()