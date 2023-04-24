"""
The platform module is used to access the underlying platform's data such as hardware, operating system and interpreter version info.
"""
import platform as pt #pip install platform
# print(dir(pt)) #to see function and variables available in the module
# print(len(dir(pt))) #to check number of of modules
# help(pt) #to read documentation

uname = pt.uname()
system = pt.system() #to fetch system name
p_version = pt.python_version() #to get your python version
P_versionT = pt.python_version_tuple() #to get your python version in tuple form
mInfo = pt.machine() #to get Machine information
release = pt.release() #to get release version
platform = pt.platform() #to get all details about release
arc = pt.architecture() #to get architecture details
proc = pt.processor() #to get processor details
node = pt.node()

print(uname)
print(system)
print(p_version)
# print(P_versionT)
print(mInfo)
print(release)
print(platform)
print(arc)
print(proc)
print(node)


"""06:24 / 15:55"""