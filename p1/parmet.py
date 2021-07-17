# coding: utf-8
from sys import argv
import sys
    
script, first = argv
py_ver =  sys.version_info.major
print ("Your python version is %d." % (py_ver))
print 
'''
The argv  variable holds the arguments you pass to your Python script
when you run it.  
     
the arguments, it gets assigned to four
variables you can work with: script, first, second, and third. This may look strange, but
“unpack” is probably the best word to describe what it does. 
It just says, “Take whatever is in
argv, unpack it, and assign it to all these variables on the left in order.”

'''
print ("The script is called:", script)
print ("Your first variable is:",  first)
#print ("Your second variable is:",  second)
 

#Prompting and Passing line  50   'learn python the hard way

 

script, user_name = argv
prompt = '> '
print ("Hi %s, I'm the %s script." % (user_name, script))


print ("I'd like to ask you a few questions.")

print ("Do you like me %s?" % user_name)
if (py_ver <3):
      likes = raw_input(prompt)
	  
else: 
      likes = input(prompt)      

print ("Where do you live %s?" % user_name)
if (py_ver < 3):
     lives =  raw_input(prompt)
else:
     lives =  input(prompt)	 
print ("What kind of computer do you have?")


if (py_ver <3):
      computer =  raw_input(prompt) 
else:
    computer =  input(prompt)  
print ("""
 Alright, so you said %r about liking me.
 You live in %r. Not sure where that is.
 And you have a %r computer. Nice.
 """ % (likes, lives, computer))