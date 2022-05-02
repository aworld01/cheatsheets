# pip install keyboard
import keyboard
from listen import listen

def key(query):
    keyboard.press_and_release('ctrl + l')
if __name__ == "__main__":
    query=listen()
    if "toolbar" in query:
        key(query)
