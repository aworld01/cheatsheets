"""Thread without arguments"""
# from threading import Thread
# def disp():
#     print('Thread Running...')
# t=Thread(target=disp)
# t.start() #starting a Thread

"""Thread with arguments"""
# from threading import Thread
# def disp(arg):
#     print('Thread Running:', arg)
# t=Thread(target=disp, args=(10,)) #Thread with arguments
# t.start()

"""Thread with MainThread"""
from threading import Thread
from time import sleep
def disp():
    for i in range(5):
        print(i,"Thread-1 Running")
        sleep(2)
t=Thread(target=disp)
t.start()

def main():
    for i in range(5):
        print(i, "MainThread is running")
        sleep(2)
main()