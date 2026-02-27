import eel #pip install eel

eel.init("www")

@eel.expose
def alert_value():
    x = "Hello, hello, how are you?"
    print(x)

eel.start("index.html", size = (600, 400))