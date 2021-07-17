#!/usr/bin/env python3
# coding: utf-8
import sys
"""
       

What it does.
\\  Backslash (\)
\'  Single- quote (')
\"  Double- quote (")
\a ASCII bell (BEL)
\b ASCII backspace (BS)
\f ASCII formfeed (FF)
\n ASCII linefeed (LF)

\r ASCII carriage return (CR)
\t ASCII horizontal tab (TAB)
"""
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
py_ver =  sys.version_info.major
print ("Your python version is %d." % (py_ver))
print(firstname)
print(lastname)

'''
We use %r for debugging, since it displays the “raw” data of the variable, but we use %s and
others for displaying to users.
'''

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print (joke_evaluation % hilarious)


formatter = "%r %r %r %r"
print ('\n')
print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
 ) )
#page 38 'learn python the hard way'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
 
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

for i in ["/","- ","|","\\","|"]:
    print ("%s\r" % i,)
#page 40 'learn python the hard way'
print ("How old are you?",) # put a (comma) at the end of each print line. This is so that
# print doesn’t end the line with a new line character and go to the next line.

if (py_ver < 3):
    age  =  raw_input('>')
else:
    age = input('>') 



print ("So, you're %r old" % (age))