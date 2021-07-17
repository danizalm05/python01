#!/usr/bin/env python3
#Learn   python  the  hard way p 74 ex20 
from sys import argv
import sys 
def print_all(f):
         print (f.read())


def rewind(f):
   f.seek(0)		 
'''	
    f.seek(offset, from_what) if omitted, 'from_what' defaults to 0
    0:   beginning of the file
    1:   current file position
    2:   end of the file
	 
'''		 
		 
def print_a_line(line_count, f):
   print (line_count, f.readline())		 
py_ver =  sys.version_info.major
print (" \n  Your python version is %d." % (py_ver))
current_file = open("ccc.txt")
print ("First let's print the whole file:\n")
print_all(current_file)         


print ("Now let's rewind, kind of like a tape.")
print (" \n  --------------------------------\n")
rewind(current_file)
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line  += 1
print_a_line(current_line, current_file)