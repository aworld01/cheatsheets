"""
subprocess module is used to execute Operating System commands
==============================================================

subprocess.run('ls') #to run a simple command

subprocess.run('ls -la', shell=True) #to run command with arguments

cmd = "ls -lrt".split() #to convert into list (["ls","-lrt"])

print(p1.stdout.decode()) #stdout.decode() converts binary into text

universal_newlines=True  #gives output as string (default output comes in byte code)

stdout=subprocess.PIPE #returns output

stderr=subprocess.PIPE #returns error

out = out.splitlines() #to convert output into list.
====================================================


comm = "ls -la"
comm2 = "ls -lrt"

shell = True (takes command in string and run in new shell)
example:
    cmd = "dir" (windows)
    cmd = "ls -lrt" (Linux)

shell = False (takes command in list and run in same shell. It does'n work on your os environment variables)
example:
    cmd = ["ls","-lrt"]

Note: stdout=subprocess.PIPE == capture_output=True
examplt:
    p1 = subprocess.run("ls -l", shell=True, capture_output=True) 

syntax:
    import subprocess as sp
    com = sp.Popen(cmd, shell=True/False, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
    rc = com.wait() #waits till executing the command (returns 0 if success, returns 1 or else if error)
    out, err = com.communicate() #returns tuple

    print(f"The return code is: {rc}")
    print()
    print(f"The output is: \n\t{out}")
    print()
    print(f"The error is: \n\t{err}")

example1:
    with open('outPut.txt', 'w') as wf:
    p1 = subprocess.run("ls -l", shell=True, stdout=wf, text=True) #to save output into textFile.

exmple2:
    file = subprocess.Popen(["mousepad", "myFile"]) #to open file with file name
    usr_inp = input("Type exit to exit: ")
    if usr_inp == "exit":
        file.terminate()
exmaple5:
    browser = subprocess.Popen(["/bin/firefox", "www.facebook.com"])
"""
import subprocess as sp

"""example1 (The output will be in byte code)"""
# cmd = "notepad"
# com = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
# rc = com.wait()
# out, err = com.communicate()

# print(f"The return code is: {rc}")
# print(type(rc))
# print()

# print(f"The output is: \n{out}")
# print(type(out))
# print()

# print(f"The error is: \n{err}")
# print(type(err))



"""example2 (The output will be in string)"""
# cmd = "notepad"
# com = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True) #The output will be in string
# rc = com.wait()
# out, err = com.communicate()

# print(f"The return code is: {rc}")
# print(type(rc))
# print()

# print(f"The output is: \n{out}")
# print(type(out))
# print()

# print(f"The error is: \n{err}")
# print(type(err))



"""example3 (The output will be converted into list)"""
# cmd = "notepad"
# com = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True) #The output will be in string
# rc = com.wait()
# out, err = com.communicate()
# out = out.splitlines() #to convert output into list.
# err = err.splitlines()

# print(f"The return code is: {rc}")
# print(type(rc))
# print()

# print(f"The output is: \n{out}")
# print(type(out))
# print()

# print(f"The error is: \n{err}")
# print(type(err))



"""example4 (open Notepad with 'myfile.txt' file name)"""
# cmd = "notepad myfile.txt"
# com = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
# rc = com.wait()
# out, err = com.communicate()
# out = out.splitlines() #to convert output into list.
# err = err.splitlines()

# print(f"The return code is: {rc}")
# print(type(rc))
# print()

# print(f"The output is: \n{out}")
# print(type(out))
# print()

# print(f"The error is: \n{err}")
# print(type(err))



"""example5 (final code)"""
# cmd = "notepad myfile.txt"
# com = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
# rc = com.wait()


"example6 "
cmd = "notepad myfile.txt"
file = sp.Popen(cmd)
usr_inp = input("Type exit to exit: ")
if usr_inp == "exit":
    file.terminate()