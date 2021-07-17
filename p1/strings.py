#!/usr/bin/env python3

'''
len('rty):  length      s.lower():lowercase    s.upper():      str(2):  turns non-strings into strings!
capitalize() - Returns the string with first letter capitalized and the rest lowercased.
casefold() - Returns a lowercase string, generally used for caseless matching. This is more 
             aggressive than the lower() method.
center() - Center the string within the specified width with optional fill character.
count() - Count the non-overlapping occurrence of supplied substring in the string.
encode() - Return the encoded version of the string as a bytes object.
endswith() - Returns true if the string ends with the supplied substring.
expandtabs() - Return a string where all the tab characters are replaced by the supplied number of spaces.
find() - Return the index of the first occurrence of supplied substring in the string. 
         Return -1 if not found.
format() - Format the given string.
format_map() - Format the given string.
index() - Return the index of the first occurrence of supplied substring in the string. 
           Raise ValueError if not found.
isalnum() - Return true if the string is non-empty and all characters are alphanumeric.
isalpha() - Return true if the string is non-empty and all characters are alphabetic.
isdecimal() - Return true if the string is non-empty and all characters are decimal characters.
isdigit() - Return true if the string is non-empty and all characters are digits.
isidentifier() - Return true if the string is a valid identifier.
islower() - Return true if the string has all lowercased characters and at least one is cased character.
isnumeric() - Return true if the string is non-empty and all characters are numeric.
isprintable() - Return true if the string is empty or all characters are printable.
isspace() - Return true if the string is non-empty and all characters are whitespaces.
istitle() - Return true if the string is non-empty and titlecased.
isupper() - Return true if the string has all uppercased characters and at least one is cased character.
join() - Concatenate strings in the provided iterable with separator between them being the string providing this method.
ljust() - Left justify the string in the provided width with optional fill characters.
lower() - Return a copy of all lowercased string.
lstrip() - Return a string with provided leading characters removed.
maketrans() - Return a translation table.
partition() - Partition the string at first occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
replace() - Replace all old substrings with new substrings.
rfind() - Return the index of the last occurrence of supplied substring in the string. Return -1 if not found.
rindex() - Return the index of the last occurrence of supplied substring in the string. Raise ValueError if not found.
rjust() - Right justify the string in the provided width with optional fill characters.
rpartition() - Partition the string at last occurrence of substring (separator) and return a 3-tuple with part before separator, the separator and part after separator.
rsplit() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the right.
rstrip() - Return a string with provided trailing characters removed.
split() - Return a list of words delimited by the provided subtring. If maximum number of split is specified, it is done from the left.
splitlines() - Return a list of lines in the string.
startswith() - Return true if the string starts with the provided substring.
strip() - Return a string with provided leading and trailing characters removed.
swapcase() - Return a string with lowercase characters converted to uppercase and vice versa.
title() - Return a title (first character of each word capitalized, others lowercased) cased string.
translate() - Return a copy of string that has been mapped according to the provided map.
upper() - Return a copy of all uppercased string.
zfill() - Return a numeric string left filled with zeros in the provided width.

Unicode String - every char represented by two strings
   unicode string  start with  'u'  
  str.encode
  str.decode   
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print ("Ah, so your name is %s , your quest is %s, " \
"and your favorite color is %s." %  (name, quest, color))
 
https://www.youtube.com/watch?v=02edODXdHgs&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=3
http://www.newthinktank.com/2016/06/learn-program-3/
Trevor Payne
https://www.youtube.com/watch?v=19EfbO5D_8s&feature=youtu.be
 ''' 

# 11:34  line  115 chmod 755 strings.py
# ---------- STRINGS ----------
# Text is stored using the string data type
# You can use type to see the data type of a value
astring = "Hello world!"
print('Does string  "Hello world!" starts with "Hello"? ', astring.startswith("Hello"))
print('Does string  "Hello world!" ends with "asd"? ', astring.endswith("asd"))


print('type(3)',type(3))
print(type(3.14))
print('type(str(3)',type(str(3))) 
# Single quotes or double are both used for strings
print(type("3"))
print(type('3'))
 
z = 10
y= "something %d" %z
print('something d ===>',y)
samp_string = "This is a very important string"

parrot = "Norwegian Blue"
print('Lower case [', parrot.lower(), ']')

print(parrot.upper())
# You can get a character by referencing an index
print(samp_string[0])
 
print(samp_string[-1]) # Get the last character
print(samp_string[3+5])
print("Length :", len(samp_string)) # String length
 
# Slice by saying where to start and end
# The 4th index isn't returned
print(samp_string[0:4])

# Get everything starting at an index
print(samp_string[8:])
 
# Join or concatenate strings with +
print("Green " + "Eggs")
 
# Repeat strings with *
print("Hello " * 5)
 
# Convert an int into a string
num_string = str(4)

# Cycle through each character with for
for char in samp_string:
    print(char)
 
# Cycle through characters in pairs
# Use range starting at index 0 through string length
# and increment by  2 each time through
for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])
 
# Computers assign characters with a number known as 
# a Unicode
# A-Z have the numbers 65-90 and a-z 97-122
 

print("A =", ord("A")) # Get the Unicode code  
 

print("65 =", chr(65)) # Convert from Unicode  

# ---------- PROBLEM : SECRET STRING ----------
# Receive a uppercase string and then hide its meaning 
# by turning  it into a string of unicodes
# Then translate it from unicode back into its 
# original meaning

norm_string = input('Enter a string to hide in uppercase(example "fff" ): ')
 
secret_string = ""
 
# Cycle through each character in the string
for char in norm_string:
 
    # Store each character code in a new string
    secret_string += str(ord(char))
 
print("Secret Message :", secret_string)
 
norm_string = ""

# Cycle through each character code 2 at a time by 
# incrementing by 2 each time through since 
# unicodes go from 65 to 90
for i in range(0, len(secret_string)-1, 2):
 
    # Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i+1]
 
    # Convert  codes into characters and add them to 
    # the new string
    norm_string += chr(int(char_code))
 
print("Original Message :", norm_string)

# ---------- SUPER AWESOME MIND SCRAMBLING PROBLEM ----------
# Make the above work with upper and lowercase with 1 addition and
# 1 subtraction
 
# Add these 2 changes
 
# secret_string += str(ord(char) - 23)
 
# norm_string += chr(int(char_code) + 23)

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
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

print ('\n\n','Method List','\n\n',dir(joke_evaluation))
print ('\n\nHelp\n\n')
print (help(joke_evaluation.count))

