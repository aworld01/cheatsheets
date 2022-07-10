import os

## to check os_module functions list
#osd = (dir(os))
# for i in osd:
#     print(i)

# os.system('clear') #to fire the Terminal commands

# path = os.listdir('.') #to check the list of any directory
# print(path)

# path = os.listdir('.')
# print(path)
# path.remove('test.py') #to remove any specific file/folder from the listdir
# print(path)

# path = os.getcwd() #to check 'current working directory'
# print(path)

# os.chdir('testings') #to change directory
# print(os.listdir('.'))

# os.makedirs('folder1/folder2') #to make recursive directories.

# os.rename('testings/file', 'file2.txt') #to rename and move the file/directory.

# os.rename('testings/file', 'file') #to move the file/directory.

# os.rename('testings/file', 'testings/file.txt') #to rename file/directory.


#os.rmdir('Files/yourdir') #to remove dir

#os.removedirs('Files/dir/dir1') #to remove all files of path


# path = os.path.exists(r'testings/') # to check existing path.
# print(path)

## to make folder if not exists
# def exst(item):
#     import os
#     if not os.path.exists(item):
#         os.makedirs(item)
# exst('my_folder')


## to check if path is file.
# n = os.path.isfile(r'testings/')
# print(n)

## to check if path is directory.
# n = os.path.isdir(r'testings/')
# print(n)



# path = r'testings'
# print(path)
# j = os.path.join(path, 'item') #to join the path
# print(j)

# path = r'testings'
# for item in os.listdir(path):
#     j = os.path.join(path, item)
#     print(j)

## os.walk
# path = r'testings'
# for path, folders, files in os.walk(path):
#     print("path: ",path)
#     print("Folders: ",folders)
#     print("Files: ",files)


import shutil

## to check shutil_module functions list
# osd = (dir(shutil))
# for i in osd:
#     print(i)

# shutil.rmtree(r'testings') #to remove complete directory

# shutil.copytree(r'testings', '../Documents/testing') #to copy complete directory with a name

# shutil.copy(r'testings/file1', '../Documents/file2') #to copy a file with a name.

# shutil.move(r'testings/file1', '../Documents/file3') #to move a file with a name.

# shutil.move(r'testings', '../Documents/testing1') #to move complete folder with a name.