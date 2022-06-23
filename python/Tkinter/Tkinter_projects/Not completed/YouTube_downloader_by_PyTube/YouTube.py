from tkinter import*
from tkinter import ttk
from pytube import*
from PIL import Image, ImageTk
import requests #pip install requests
import io
import os

class Youtube_app:
    def __init__(self, root):
        self.root=root
        self.root.title("YouTube Downloader")
        self.root.geometry("500x420+300+50")
        self.root.resizable(0,0)
        self.root.config(bg="white")
        pt = PhotoImage(file = 'icon.png')
        root.iconphoto(False, pt)

        """Title"""
        Label(self.root, text="YouTube Downloader | Developed by Abdul Zoha", font=("times new roman", 15), bg="#262626", fg="white").pack(fill=X)

        """URL"""
        Label(self.root, text="Video URL: ", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=50)
        self.var_url = StringVar()
        self.ent = Entry(self.root, font=("times new roman", 13), bg="lightyellow", textvariable=self.var_url).place(x=120, y=50, width=340)

        """file_type"""
        Label(self.root, text="File Type: ", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=90)
        self.var_file_type = StringVar()
        self.var_file_type.set("Video")
        audio = Radiobutton(self.root, text="Audio: ", font=("times new roman", 15, "bold"), bg="white", activebackground="white", variable=self.var_file_type, value="Audio")
        audio.place(x=120, y=90)
        video = Radiobutton(self.root, text="Video: ", font=("times new roman", 15, "bold"), bg="white", activebackground="white", variable=self.var_file_type, value="Video")
        video.place(x=220, y=90)
        """Search Button"""
        Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="blue", fg="white", command=self.search).place(x=350, y=90, height=30, width=110)

        """video"""
        frm = Frame(self.root, bd=2, relief=RIDGE, bg="lightyellow")
        frm.place(x=10, y=130, width=480, height=180)

        self.video_title = Label(frm, text="Video Title Here: ", font=("times new roman", 12), bg="lightgray", anchor=W)
        self.video_title.place(x=0, y=0, relwidth=1)

        self.video_image = Label(frm, text="Video\nImage", font=("times new roman", 15), bg="lightgray", bd=2, relief=RIDGE)
        self.video_image.place(x=5, y=30, width=180, height=140)

        lbl_desc = Label(frm, text="Description: ", font=("times new roman", 15), bg="lightyellow").place(x=190, y=30)

        self.video_desc = Text(frm, font=("times new roman", 12), bg="lightyellow")
        self.video_desc.place(x=190, y=60, width=280, height=110)

        self.lbl_size = Label(self.root, text="Total size:", font=("times new roman", 13, "bold"), bg="white")
        self.lbl_size.place(x=10, y=320)

        self.lbl_percentage = Label(self.root, text="Downloading: 0%", font=("times new roman", 13, "bold"), bg="white")
        self.lbl_percentage.place(x=165, y=320)

        clear_btn = Button(self.root, text="Clear", font=("times new roman", 13, "bold"), bg="gray", fg="white", command=self.clear).place(x=328, y=320, width=70, height=25)

        self.btn_download = Button(self.root, text="Download", font=("times new roman", 13, "bold"), bg="green", fg="white", command=self.download, state=DISABLED)
        self.btn_download.place(x=400, y=320, width=90, height=25)

        """Status"""
        self.lbl_message = Label(self.root, text="", font=("times new roman", 13, "bold"), bg="white")
        self.lbl_message.place(x=0, y=385, relwidth=1)

        """ProgressBar"""
        self.prog = ttk.Progressbar(self.root, orient=HORIZONTAL, length=590, mode="determinate")
        self.prog.place(x=10, y=360, width=480, height=20)

        """directory validation"""
        if not os.path.exists("audios"):
            os.mkdir("audios")
        elif not os.path.exists("videos"):
            os.mkdir("videos")
  
    def search(self):
        if self.var_url.get() == "":
            self.lbl_message.config(text="Video URL is required!", fg="red")
        else:
            url = self.var_url.get()
            yt = YouTube(url)
            title = yt.title
            desc = yt.description[:200]

            """fetch the file as per type"""
            if self.var_file_type.get() == "Video":
                select_file = yt.streams.filter(progressive=True).first()
            elif self.var_file_type.get() == "Audio":
                select_file = yt.streams.filter(only_audio=True).first()

            self.size_in_bytes = select_file.filesize
            self.max_size = self.size_in_bytes/1024000
            self.mb = str(round(self.max_size, 2))+"MB"
            self.lbl_size.config(text="Total size: "+self.mb)

            """thumbnail"""
            thumbnail = yt.thumbnail_url
            response = requests.get(thumbnail)
            img_byte = io.BytesIO(response.content)
            self.img = Image.open(img_byte)
            self.img = self.img.resize((180,140),Image.ANTIALIAS) #(width, height)
            self.img = ImageTk.PhotoImage(self.img)

            """updating the frame elements"""
            self.video_image.config(image=self.img)
            self.video_title.config(text=title)
            self.video_desc.delete("1.0", END)
            self.video_desc.insert(END, desc)
            self.btn_download.config(state=NORMAL)
    def progress_(self, streams, chunk, bytes_remaining):
        percentage = (float(abs(bytes_remaining-self.size_in_bytes)/self.size_in_bytes))*float(100)
        self.prog["value"]=percentage
        self.prog.update()
        self.lbl_percentage.config(text=f"Downloading: {str(round(percentage,2))}%")
        if round(percentage,2) == 100:
            self.lbl_message.config(text="Download Completed", fg="green")
            self.btn_download.config(state=DISABLED)
    def download(self):
        yt = YouTube(self.var_url.get(), on_progress_callback = self.progress_)
        if self.var_file_type.get() == "Video":
            select_file = yt.streams.filter(progressive=True).first()
            select_file.download("videos")
        elif self.var_file_type.get() == "Audio":
            select_file = yt.streams.filter(only_audio=True).first()
            select_file.download("audios")
    def clear(self):
        self.var_file_type.set("Video")
        self.var_url.set("")
        self.prog["value"] = 0
        self.btn_download.config(state=DISABLED)
        self.lbl_message.config(text="")
        self.video_title.config(text="Video Title Here: ")
        self.video_image.config(image="")
        self.video_desc.delete(1.0, END)
        self.lbl_percentage.config(text="Downloading: 0%")
        self.lbl_size.config(text="Total size:")
root = Tk()
obj = Youtube_app(root)
root.mainloop()