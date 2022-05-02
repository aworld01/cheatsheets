from tkinter import*
from tkinter import messagebox
import random

from matplotlib.pyplot import fill

eng = [
    "something is better than nothing",
    "how did you know",
    "what is your name",
    "how do you do",
    "what's up",
]
hin = [
    "कुछ होना कुछ नहीं होने से बेहतर है",
    "आपको कैसे पता चला",
    "आपका नाम क्या है",
    "आप कैसे हैं",
    "क्या चल रहा है"
]

hit = 0
miss = 0
total = 0
n = len(eng)
num = random.randrange(0,n,1)

"""functions"""
def default():
    global eng, hin, num
    lbl.config(text=hin[num])
def reset():
    global hin, eng, num
    num = random.randrange(0,n,1)
    lbl.config(text=hin[num])
    ans.config(text="")
    ent.delete(0, END)
def check(key):
    global hin, eng, num, hit, total, miss
    word = ent.get()
    if word == eng[num]:
        ent.delete(0, END)
        hit += 1
        total += 1
        hit_lbl.config(text=f"{hit}")
        total_lbl.config(text=f"{total}")
        reset()
    elif word == "":
        messagebox.showinfo("Information", "The User input can't be empty")
    elif word == "exit()":
        root.destroy()
    else:
        ans.config(text=f"The right answer is: {eng[num]}")
        miss += 1
        hit -= 1
        total += 1
        mis_lbl.config(text=f"{miss}")
        hit_lbl.config(text=f"{hit}")
        total_lbl.config(text=f"{total}")

root = Tk()
root.title("English Word Game")
root.geometry("900x500+1200+100")
root.config(bg="#000000")
"""Label"""
lbl = Label(root, font=("Verdana", 18), bg="#000000", fg="#ffffff")
lbl.pack(pady=40)
"""Entry"""
ent = Entry(root, font=("verdana", 16))
ent.pack(ipadx=300)

frm = Frame(root, bg="#000000")
frm.pack(pady=(40, 0))

Label(frm, text="Hit: ", bg="#000000", fg="#ffffff").grid(row=0, column=0, sticky=W)
hit_lbl = Label(frm, text="O", bg="#000000", fg="#ffffff")
hit_lbl.grid(row=0, column=1)

Label(frm, text="Miss: ", bg="#000000", fg="#ffffff").grid(row=1, column=0, sticky=W)
mis_lbl = Label(frm, text="O", bg="#000000", fg="#ffffff")
mis_lbl.grid(row=1, column=1)

Label(frm, text="Total: ", bg="#000000", fg="#ffffff").grid(row=2, column=0, sticky=W)
total_lbl = Label(frm, text="O", bg="#000000", fg="#ffffff")
total_lbl.grid(row=2, column=1)

"""Label"""
ans = Label(root, font=("Verdana", 18), bg="#000000", fg="#ffffff")
ans.pack(pady=40)


root.bind("<Return>", check) #Enter check
default()

root.mainloop()