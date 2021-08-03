"""
Minimum example to introduce sys.argv
C:\Users\gilfm\Miniconda3\python.exe
C:/Users/gilfm/Documents/d/python01/opencv/alberto-fernandaz/img-procesing/Chapter03/01-chapter-content/sysargv_python.py vvvvvvvvvv
"""

# Import the required packages
import sys

# We will print some information in connection with sys.argv to see how it works:
print("The name of the script being processed is: '{}'".format(sys.argv[0]))
print("The number of arguments of the script is: '{}'".format(len(sys.argv)))
print("The arguments of the script are: '{}'".format(str(sys.argv)))
