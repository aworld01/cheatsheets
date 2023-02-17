import eel #pip install eel

eel.init("www")

@eel.expose
def alert_value(x):
    return x

eel.start("index.html", size = (600, 400))