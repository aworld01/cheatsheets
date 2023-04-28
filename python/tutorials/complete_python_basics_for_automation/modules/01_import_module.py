"""
Import either default or third party modules before using them.

There are defferent ways to importing module:-
    import fileOne #import only module
    print(fileOne.sum(5,6)) #you can use all the functions in module

    from fileOne import sum #import only sum function
    print(sum(5,6)) #you can use only one function that is imported

    from fileOne import* #import all
    print(sum(5,6)) #you can use all the functions in module

    import fileOne as f #import module and giving that alias as f
    print(sum(5,6)) #you can use only one function that is imported

    EXAMPLE1
    ========
    import platform
    import math
    import sys
    import os
    import subprocess

    EXAMPLE2
    import platform, math, sys, os, subprocess


"""
"""example1"""
# import os
# print(fileOne.sum(5,6)) #you can use all the functions in module

"""example2"""
# from os import listdir
# print(sum(5,6)) #you can use only one function that is imported

"""example3"""
# from os import*
# print(sum(5,6)) #you can use all the functions in module

"""example4"""
import os as o #import module and giving that alias as f
print(o.sum(5,6)) #you can use all the functions in module