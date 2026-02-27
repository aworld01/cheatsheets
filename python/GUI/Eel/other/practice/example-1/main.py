import eel

@eel.expose
def sort(text):
    answer = sorted([float(num) for num in text.split(",")])
    eel.showAnswers(answer)

eel.init("www")
eel.start("index.html", size=(600, 400))