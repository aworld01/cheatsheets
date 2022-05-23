from threading import Thread, current_thread

"""to get thread object / current_thread() #Thread_name, status, identity number"""
# def disp():
#   print('Child Thread object:', current_thread()) #to get current_thread object
# t=Thread(target=disp)
# t.start()
# print('Main Thread', current_thread())


"""to get thread name"""
# def disp():
#     t_name = current_thread()
#     print('ChildThread name:', t_name.name) #to get current_thread name
# t=Thread(target=disp)
# t.start()

# main = current_thread()
# print('MainThread name:', main.name)


"""to set thread name"""
# def disp():
#     thread1 = current_thread()
#     print('ChildThread name:', thread1.name)
#     thread1.name = "New born" #to set current_thread name
#     print('ChildThread name:', thread1.name)
# t=Thread(target=disp)
# t.start()

# main = current_thread()
# print('MainThread name:', main.name)
# main.name = "Father" #to set current_thread name
# print('MainThread name:', current_thread().name)



"""change thread name by object"""
# def disp():
#     pass

# t=Thread(target=disp)
# print("ChildThread name:", t.name) #to get thread name
# t.name = "New born" #to set thread name
# print("ChildThread name:", t.name)

# main = current_thread()
# print('MainThread name:', main.name)
# main.name = "Father" #to set current_thread name
# print('MainThread name:', main.name)



"""set thread default name"""
def disp():
    pass

t=Thread(target=disp, name = "New Thread")
print("ChildThread name:", t.name)