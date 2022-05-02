import os, shutil
# function to make a file/folder if not exist.
def exst(item):
  if not os.path.exists(item):
    os.makedirs(item)
    

files = os.listdir()
files.remove("main.py")

imgs = [".png",".jpg",".jpeg"]
docs = [".txt",".doc",".docx",".html",".pdf"]
meds = [".mp3",".mp4",".flv"]


for file in files:
  if os.path.splitext(file)[1].lower() in imgs: # to findout file by extensions
    exst("images")
    shutil.move(file, "images")
  
for file in files:
  if os.path.splitext(file)[1].lower() in docs:
    exst("documents")
    shutil.move(file, "documents")
    
for file in files:
  if os.path.splitext(file)[1].lower() in meds:
    exst("media")
    shutil.move(file, "media")
  
for file in files:
  ext = os.path.splitext(file)[1].lower()
  # os.path.isfile() to findout only file
  if (ext not in imgs) and (ext not in docs) and (ext not in meds) and os.path.isfile(file):
    exst("others")
    shutil.move(file, "others")