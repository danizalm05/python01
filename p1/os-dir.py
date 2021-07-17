 
import sys
import os
'''
When a module is loaded in Python, __file__ is set to its name. You can 
then use that with  other functions to find the directory that the file 
is located in.
os.chdir(path): change the current working directory to path 
os.getcwd(): Current working directory
os.name: 
'''
py_ver =  sys.version_info.major
print("\n\nYour python version is %d." % py_ver)
print("OS name %s." % os.name)
cwd = os.getcwd()
print ("Current working directory %s  " % cwd)
dir_name = os.path.dirname(cwd)
print ("Directory name of pathname  %s  " % dir_name)

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file directory and name")
print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print("Full_path", full_path + "\n\n")

path, filename = os.path.split(full_path)
print(path + '\ ' + filename)

pr = os.path.join(os.path.dirname(__file__), '..')
# A is the parent directory of the directory where program resides.
print("Parent directory %s." % pr)

PATH = 1

try:
    dr = sys.argv[PATH]
    print("List of files in directory %s." % pr)
    print os.listdir(dr)
except Exception, e:
    print (e)
finally:
    print('End of directory scan')
