import os

# print(os.getcwd()) #to get path of current working directory

# os.mkdir('Movies') #to make a single folder if not exist

"""example-1"""
# print(os.path.exists('Movies')) #to check existing path (case sensetive)
"""example-2"""
# if not os.path.exists('Movies'):
#     os.mkdir('Movies')

# os.makedirs("new/movies/Tere Naam") #to make directories recursively

# open('file.txt','a').close() #to create an empty file

# os.chdir('/home/thor/Desktop') #to change directory
# print(os.getcwd())

"""example-1"""
# l = os.listdir('/home/thor') #to get list of all files and folders
# print(l)

"""example-2"""
# path = r"/home/thor/Documents"
# for item in os.listdir(path):
#     data = path+"/"+item
#     print(data)

# path = r"/home/thor/Documents"
# for item in os.listdir(path):
#     data = os.path.join(path, item) #to join path and item
#     print(data)

# path = r"/home/thor/Documents"
# for path, dirs, files in os.walk(path):
#     print(f"Path: {path}")
#     print(f"\tFolders: {dirs}")
#     print(f"\t\tFiles: {files}")

# os.rmdir('demo2') #to delete an empty folder