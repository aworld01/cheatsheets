"""
subprocess module is used to execute Operating System commands
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
=========================================================================

cmd = "ls -lrt".split() #to convert into list (["ls","-lrt"])

universal_newlines=True #to take output in string (output comes in byte code without it)

out = out.splitlines() #to convert output into list.

shell = True (takes command in string and run in new shell)
example:
    cmd = "dir" (windows)
    cmd = "ls -lrt" (Linux)

shell = False (takes command in list and run in same shell)
example:
    cmd = ["ls","-lrt"]

    
15:00 / 28:16
"""
import subprocess as sp

"""example1 (The output will be in byte code)"""
# cmd = "dir"
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
# cmd = "dir"
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
cmd = "dir"
com = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True) #The output will be in string
rc = com.wait()
out, err = com.communicate()
out = out.splitlines() #to convert output into list.
err = err.splitlines()

print(f"The return code is: {rc}")
print(type(rc))
print()

print(f"The output is: \n{out}")
print(type(out))
print()

print(f"The error is: \n{err}")
print(type(err))