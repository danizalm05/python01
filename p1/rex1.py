#!/usr/bin/env python3
#          15 : Regular Expressions (Regex)
# https://www.youtube.com/watch?v=R1PcJfzsUU0&index=15&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwthttp://www.newthinktank.com/2016/07/learn-program-8/
# Regular expressions allow you to locate and change
# strings in very powerful ways.
# They work in almost exactly the same way in every
# programming language as  well.

# Regular Expressions (Regex) are used to
# 1. Search for a specific string in a large amount of data
# 2. Verify that a string has the proper format (Email, Phone #)
# 3. Find a string and replace it with another string
# 4. Format data into the proper form for importing for example


import re  # import the Regex module

# ---------- Was a Match Found ----------

# Search for ape in the string
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# ---------- Get All Matches ----------

# findall() returns a list of matches
# . is used to match any 1 character or space
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

# finditer returns an iterator of matching objects
# You can use span to get the location

theStr = "The ape was at the apex"
for i in re.finditer("ape.", theStr):
    locTuple = i.span()  # Span returns a tuple
    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])  # Slice the match out using the tuple values

# ---------- Match 1 of Several Letters ----------

# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties
# unless they are listed

animalStr = "Cat rat mat fat pat"

allAnimals = re.findall("[crmfp]at", animalStr)
for i in allAnimals:
    print(i)
print()
print("characters in a range")
print("-------------")


# We can also allow for characters in a range
# Remember to include upper and lowercase letters
someAnimals = re.findall("[c-mC-M]at", animalStr)
for i in someAnimals:
    print(i)

print()

# Use ^ to denote any character but whatever characters are
# between the brackets
someAnimals = re.findall("[^Cr]at", animalStr)
for i in someAnimals:
    print(i)

print()

# ---------- Replace All Matches ----------

# Replace matching items in a string

owlFood = "rat cat mat pat"

# You can compile a regex into pattern objects which
# provide additional methods
regex = re.compile("[cr]at")

# sub() replaces items that match the regex in the string
# with the 1st attribute string passed to sub
owlFood = regex.sub("owl", owlFood)

print(owlFood)

# ---------- Solving Backslash Problems ----------

# Regex use the backslash to designate special characters
# and Python does the same inside strings which causes
# issues.

# Let's try to get "\\stuff" out of a string

randStr = "Here is \\stuff"

# This won't find it
print("Find \\stuff : ", re.search("\\stuff", randStr))

# This does, but we have to put in 4 slashes which is
# messy
print("Find \\stuff : ", re.search("\\\\stuff", randStr))

# You can get around this by using raw strings which
# don't treat backslashes as special
print("Find \\stuff : ", re.search(r"\\stuff", randStr))

# ---------- Matching Any Character ----------
# We saw that . matches any character, but what if we
# want to match a period. Backslash the period
# You do the same with [, ] and others

randStr = "F.B.I. I.R.S. CIA"

print("findall = ",(re.findall(".\..\.", randStr)))
# output findall =  ['F.B.', 'I.R.']
print("findall = ",(re.findall(".\..\..", randStr)))
# output  findall =  ['F.B.I', 'I.R.S']
print("Matches :", len(re.findall(".\..\..", randStr)))
# output  Matches : 2
# ---------- Matching Whitespace ----------
# We can match many whitespace characters

randStr = """This is a long
string that goes
on for many lines"""

print(randStr)

regex = re.compile("\n") # Remove newlines
randStr = regex.sub("-", randStr)
print("Remove newlines randStr =",randStr)
# print Remove newlines randStr = This is a long-string that goes-on for many lines

# You can also match
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# You may need to remove \r\n on Windows

# ---------- Matching Any Single Number ----------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]

randStr = "12345"
print("re.findall('\d', randStr)", re.findall("\d", randStr))
# prints re.findall('\d', randStr) ['1', '2', '3', '4', '5']
print("Matches :", len(re.findall("\d", randStr)))

# ---------- Matching Multiple Numbers ----------
# You can match multiple digits by following the \d with {numOfValues}

# Match 5 numbers only
if re.search("\d{5}", "12345"):# five numbers
    print("It is a zip code")

# You can also match within a range
# Match values that are between 5 and 7 digits
numStr = "123 12345 123456 1234567"
print(re.findall("\d{5,7}", numStr))  # ['12345', '123456', '1234567']
print("Matches :", len(re.findall("\d{5,7}", numStr)))

# ---------- Matching Any Single Letter or Number ----------
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]

phNum = "412-555-1212"

# Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

# Check for valid first name between 2 and 20 characters
if re.search("\w{2,20}", "Ultraman"):
    print("It is a valid name")

# ---------- Matching WhiteSpace ----------
# \s is the same as [\f\n\r\t\v] ( s= space)
# \S is the same as [^\f\n\r\t\v]

# Check for valid first and last name with a space
if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("It is a valid full name")

# ---------- Matching One or More ----------
# + matches 1 or more characters

# Match a followed by 1 or more characters
print("Matches :", (re.findall("a+", "a as ape bug")))
# Matches : ['a', 'a', 'a']
# ---------- Problem ----------
# Create a Regex that matches email addresses from a list
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

emailList = "db@aol.com m@.com @apple.com db@.com"
e = re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emailList)
print(e)  # ['db@aol.com']
