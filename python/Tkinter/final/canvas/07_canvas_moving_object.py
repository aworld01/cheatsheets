from tkinter import*
from turtle import color

class Move:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Canvas : Move")

        """creating Canvas"""
        self.can = Canvas(self.root, width=400, height=400, bg="white")
        self.can.pack(pady=20)
        """creating rectangle"""
        self.rec = self.can.create_rectangle(200, 200, 300, 300, fill="red") #x_pos, y_pos, width, height
        self.moving()

    def moving(self):
        """to move rectangle"""
        side = self.can.bbox(self.rec)
        print(side)
        x1, y1, x2, y2 = side
        if x1<1 and y2<400:
            self.can.move(self.rec, 0, 10)
        elif y2>400 and x2<400:
            self.can.move(self.rec, 10, 0)
        elif x2>400 and y1>1:
            self.can.move(self.rec, 0, -10)
        else:
            self.can.move(self.rec, -10, 0)
            
        self.root.after(100, self.moving)

if __name__ == "__main__":
    root = Tk()
    obj = Move(root)
    root.mainloop()