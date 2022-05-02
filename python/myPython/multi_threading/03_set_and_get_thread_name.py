from threading import Thread, current_thread

"""to get thread object / current_thread() #Thread_name, status, identity number"""
# def disp():
#   print('Child Thread object:', current_thread()) #to get current_thread object
# t=Thread(target=disp)
# t.start()
# print('Main Thread', current_thread())


"""to get thread name"""
# def disp():
#   print('ChildThread name:', current_thread().name) #to get current_thread name
# t=Thread(target=disp)
# t.start()
# print('MainThread name:', current_thread().name)


"""to set thread name"""
# def disp():
#   print('ChildThread name:', current_thread().name)
#   current_thread().name = "New born" #to set current_thread name
#   print('ChildThread name:', current_thread().name)
# t=Thread(target=disp)
# t.start()
# print('MainThread name:', current_thread().name)
# current_thread().name = "Father" #to set current_thread name
# print('MainThread name:', current_thread().name)



"""change thread name by object"""
# def disp():
#     pass

# t=Thread(target=disp)
# print('MainThread name:', current_thread().name)
# current_thread().name = "Father" #to set current_thread name
# print('MainThread name:', current_thread().name)

# print("ChildThread name:", t.name) #to get thread name
# t.name = "New born" #to set thread name
# print("ChildThread name:", t.name)



"""set thread default name"""
def disp():
    pass

t=Thread(target=disp, name = "New Thread")
print("ChildThread name:", t.name)