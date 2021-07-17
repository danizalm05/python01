#!/usr/bin/env python3
#          8 : TUPLES
# https://www.youtube.com/watch?v=EukxMIsNeqU&index=8&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt
# http://www.newthinktank.com/2016/07/learn-program-8/

# 17:10 line 182
# A Tuple is like a list, but their values can't be changed
# Tuples are surrounded with parentheses instead of
# square brackets

myTuple = (1, 2, 3, 5, 8)

# Get a value with an index
print("Tuple 1st Value :", myTuple[0])

# Get a slice from the 1st index up to but not including
# the 3rd
print("slice", myTuple[0:3])

# Get the number of items in a Tuple
print("Tuple Length :", len(myTuple))

# Join or concatenate tuples
moreFibs = myTuple + (13, 21, 34)

# Check if a value is in a Tuple
print("34 in Tuple :", 34 in moreFibs)

# Iterate through a tuple
for i in moreFibs:
    print(i)

# Convert a List into a Tuple
aList = [55, 89, 144]
aTuple = tuple(aList)

# Convert a Tuple into a List
aList = list(aTuple)

# Get max and minimum value
print("Min :", min(aTuple))
print("Max :", max(aTuple))

print "this is a tuple: %s" % (aTuple,)