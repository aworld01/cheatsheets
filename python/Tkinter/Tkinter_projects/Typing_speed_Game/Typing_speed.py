from tkinter import *
import random
from tkinter import messagebox

words = ['Mango', 'Apple', 'Banana', 'Grapes']

##########################################################Functions################################################
def slider():
    global count, sliderwords
    text='Welcome to Typing speed Game...'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    font.config(text=sliderwords)
    font.after(100, slider)

def time():
    global timeleft, score, miss
    if(timeleft >= 11):
        pass
    else:
        timeLabelCount.config(fg='red')
    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.config(text=timeleft)
        timeLabelCount.after(1000, time)
    else:
        hint.config(text='Hit = {} | Miss = {} | Total Score = {}'.format(score, miss, score-miss))
        rr = messagebox.askretrycancel('Notification', 'For play again Hit Retry')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.config(text=timeleft)
            word.config(text=world[0])
            scoreLabelCount.config(text=score)

def startGame(event):
    global score, miss
    if(timeleft == 60):
        time()
    hint.config(text='')
    if(wEntry.get() == word['text']):
        score += 1
        scoreLabelCount.config(text=score)
    else:
        miss += 1
        scoreLabelCount.config(text=score)
    ##to change worlds
    random.shuffle(words)
    word.config(text=words[0])
    wEntry.delete(0, END) #to clear Entry box after hit Enter.

##########################################################Root_Method################################################
root = Tk()
root.geometry('800x600+400+100')
root.config(bg='powder blue')
root.title('Typing speed Game')
pt = PhotoImage(file = 'css.png')
root.iconphoto(False, pt)

##########################################################Variables####################################################
score = 0
miss = 0
timeleft = 60
count = 0
sliderwords = ''

##########################################################Label_Methods################################################
font = Label(
    root,
    text='',
    font=('arial', 25, 'italic bold'),
    width=40,
    bg='powder blue',
    fg='red'
)
font.place(x=10, y=10)
slider()

random.shuffle(words)
word = Label(
    root,
    text=words[0],
    font=('arial', 40, 'italic bold'),
    bg='powder blue',
    fg='red'
)
word.place(x=350, y=200)

scoreLabel = Label(
    root,
    text='Your score: ',
    font=('arial', 25, 'italic bold'),
    bg='powder blue'
)
scoreLabel.place(x=10, y=100)

scoreLabelCount = Label(
    root,
    text=score,
    font=('arial', 25, 'italic bold'),
    bg='powder blue',
    fg='blue'
)
scoreLabelCount.place(x=80, y=180)

timerLabel = Label(
    root,
    text='Time left: ',
    font=('arial', 25, 'italic bold'),
    bg='powder blue'
)
timerLabel.place(x=600, y=100)

timeLabelCount = Label(
    root,
    text=timeleft,
    font=('arial', 25, 'italic bold'),
    bg='powder blue',
    fg='blue'
)
timeLabelCount.place(x=600, y=180)

hint = Label(
    root,
    text='Tips: Type World And Hit Enter',
    font=('arial', 30, 'italic bold'),
    bg='powder blue',
    fg='dark grey'
)
hint.place(x=120, y=450)

##########################################################Entry_Methods################################################
wEntry = Entry(
    root,
    font=('arial', 25, 'italic bold'),
    justify='center', #to start typing from center
    bd=5
)
wEntry.place(x=220, y=300)
wEntry.focus_set() #to start typing without click in entrybox

root.bind('<Return>', startGame) #to action perform by hit Enter

root.mainloop()