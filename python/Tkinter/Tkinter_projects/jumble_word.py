from tkinter import*
from tkinter import messagebox
import random

answers = [
    "america",
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "london",
    "delhi",
    "germany",
    "bhutan",
    "russia",
    "australia",
    "brazil",
    "beijing",
    "mexico",
    "mumbai",
    "tokyo",
    "cairo",
    "japan",
    "france",
    "singapore",
    "iran",
    "indonesia",
    "italy",
    "sweden"
]
words = [
    "aiearcm",
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "odnlon",
    "dlhei",
    "graeynm",
    "buahtn",
    "irsaus",
    "asuaairlt",
    "bzairl",
    "binegij",
    "xcmoie",
    "mmauib",
    "tokoy",
    "cioar",
    "ajnpa",
    "nfcear",
    "segonpari",
    "anir",
    "iedsanino",
    "iaytl",
    "dseewn"
]
num = random.randrange(0,25,1)
"""functions"""
def default():
    global answers, words, num
    lbl.config(text=words[num])
def reset():
    global words, answers, num
    num = random.randrange(0,25,1)
    lbl.config(text=words[num])
    ent.delete(0, END)
def check(key):
    global words, answers, num
    word = ent.get()
    if word == answers[num]:
        ent.delete(0, END)
        reset()
    elif word == "":
        messagebox.showinfo("Information", "The User input can't be empty")
    else:
        ans.config(text=f"The right answer is: {answers[num]}")

root = Tk()
root.title("Jumbbled word game...")
root.geometry("400x500+1200+100")
root.config(bg="#000000")
"""Label"""
lbl = Label(root, font=("Verdana", 18), bg="#000000", fg="#ffffff")
lbl.pack(pady=40)
"""Entry"""
ent = Entry(root, font=("verdana", 16))
ent.pack()
"""Button"""
btn_check = Button(root, text="Check", font=("comic sans ms", 16), width=16, bg="#4C4848", fg="#6ab04c", command=lambda:check("key"))
btn_check.pack(pady=40)

btn_reset = Button(root, text="Reset", font=("comic sans ms", 16), width=16, bg="#4C4848", fg="#EA425C", command=reset)
btn_reset.pack()
"""Label"""
ans = Label(root, text="The right answer is: ", font=("Verdana", 18), bg="#000000", fg="#ffffff")
ans.pack(pady=40)


root.bind("<Return>", check) #Enter: to exit
default()

root.mainloop()