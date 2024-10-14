"""
Tutorial 28 - Using os.listdir to read multiple files
returns a list containing the names of the entries in the directory given by path

https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial28_using_os.listdir_to_read_multiple_images.py
https://www.youtube.com/watch?v=j6GNtqrwcNE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=29
2:41
"""

import getpass
import os


USER = getpass.getuser()

IMAGE_NAME = '1.jpg'
BASE_FOLDER = 'C:/Users/' + USER + '/Pictures/Saved Pictures/'
IMAGE = BASE_FOLDER + IMAGE_NAME

path = BASE_FOLDER
file_list = os.listdir(path)
print(file_list)  #Very similar to glob, prints a list of all files in the directory

for (image) in os.listdir(path):  #iterate through each file to perform some action
    print(image)

for i, file in enumerate(file_list, start=1):
    print(i,file)    
    
"""
#os.walk --     
returns a generator, that creates a tuple of values 
(current_path, directories in current_path, files in current_path).   

Every time the generator is called it will follow each directory 
recursively  until no further sub-directories are available from the 
initial directory  that walk was called upon.

os.path.join() method in Python join one or more path components 
intelligently.
""" 
print("\n\n        os.walk\n---------------------------\n") 
print(os.walk("."))  #Nothing to see here as this is just a generator

#object

# traverse root directory, and list directories as dirs and files as 
#files
#alk_str = "."#local dir
walk_str = 'C:/Users/' + USER + '/Pictures/'
for (root,  dirs,  files)  in  os.walk(walk_str):
    print("root = ",root)  #Prints root directory names
    
    path = root.split(os.sep)  #SPlit at separator (/ or \)
    #print(path)  #Gives names of directories for easy location of files

    
#Let us now visualize directories and files within them
    #Add --- based on the path
    print((len(path) - 1) * '---', os.path.basename(root)) 
    
    for file in files:
        print(len(path) * '---', file)

    #######################
    # Another way to look at all dirs. and files...


for root, dirs, files in os.walk("."):
    # for path,subdir,files in os.walk("."):
    print('\n start name in dirs\n====\n' )

    for name in dirs:
        print(os.path.join(root, name))  # will print path of directories
    print('\n end name in dirs\n-----------------\n')
    print('\n start name in files\n**********\n')
    for name in files:
        print(os.path.join(root, name))  # will print path of files
    print('\n end name in files\n++++++++++++++++++\n')