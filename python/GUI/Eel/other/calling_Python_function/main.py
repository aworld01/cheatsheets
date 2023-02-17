import eel #pip install eel

eel.init("html") #html dir path

@eel.expose
def alert_value(x):
    return x

eel.start("index.html", size=(500,500)) #htmlFile