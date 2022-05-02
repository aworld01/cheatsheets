import threading

name = threading.current_thread().name #to get Current Thread Name
print('The current_thread name is:', name)