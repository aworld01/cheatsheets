import eel
from datetime import datetime as dt

eel.init("www")
eel.start("index.html", block = False)

while True:
    print("Hello world")