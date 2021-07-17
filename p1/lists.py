import math
"""
list
la = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
la = str.split('@') # create list from a string Sprating char is '@'
la = str.split()    # create list from a string Sprating char is ' '
str = '*'.join(la)  # Create a string from a list
L.append('asw')    # Add item as last item
L +=  'asw'        # Add item as last item
l[i] = 'fff'       # Change item in index i
L.clear()          # remove all items from L
L.index(value, [start, [stop]]) #- return first index of value.
                                   Raises ValueError if the value is not present.
L.count(value)     # return number of occurrences of value
L.insert(index, object)# insert object before index
L.extend(iterable) # extend list by appending elements from the iterable

L.pop(0)           # pull  1'st item from a list
L.sort()           # Sort a list
L.remove(value)    # Remove first occurrence of value.
L.reverse()        # Reverse a list
L.sort(reverse=True)  # Reverse a list
L.sort(key=len)     #sort according to length


la= str.split('#') #

maxL = max(L)
newL = sorted(L) # Returns  a new list
newL = sorted(L,key=len) # Returns  the sorted  list
                          according to length of item

list comprehensions

-------------------------
s= [i**2 for i in range(100) if i%2==0] Create  list of x**2 for even numbers

"""
# Create list of prime number smaller than 100
LIMIT = 100
non_primes = []
root = int(math.sqrt(LIMIT))# root=10
for i  in range (2,root):  #2 to 9

  for j in range(2*i , LIMIT, i):
     #2-4:98, 3-6:99, 4-8:96, 5-10:95, 6-12:96, 7-14:98 ,8-16:96,9-18:99

        non_primes.append(j)
non_primes.sort() # LIST of non prime numbers up to 100
primes = []
for i in range(LIMIT):
    if i not in non_primes:
        primes.append(i)

print("List of prime numbers below 100 = {}".format(primes))

def last_char(s):
    return s[-1]


ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')

i = 0
for e in stuff:
    print(i, e)
    i = i + 1
stuff.sort(key=len)  # sort according to length
print("Result of \'stuff.sort(key = len)\'")
print(stuff)
stuff.sort(key=last_char)  # sort according to last char
print("Result of \'stuff.sort(key = last_char)\'")
print(stuff)

print("Wait there's not 10 things in that list, let's fix that.")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
fstr = 'Boy'
if fstr in more_stuff:
    print("String %s is in list more_stuff" % fstr)

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff)
print("Let's do some things with stuff.")
print(stuff[1])  # Second item
print(stuff[- 1])  # Last  item
print(stuff.pop())  # Take out last item
print(' '.join(stuff))  # Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
print('#'.join(stuff[3:5]))  # Telephone#Light

# Lists 130    'learn python the hard way'


# Loops and Lists  106     'learn python the hard way'
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for- loop goes through a list

for number in the_count:
    print("This is count %d" % number)
# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)

# Loops and Lists  110     'learn python the hard way'


# https://www.youtube.com/watch?v=A1HUzrvS-Pw
# http://www.newthinktank.com/2016/07/learn-program-6/

import random
import math

# Each item in the list corresponds to a number (index)
# just like how people have identification numbers.
# By default the 1st item in a list has the index 0

# [0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]

# Python lists can grow in size and can contain data
# of any type

randList = ["string", 1.234, 28]
# Create a list with range
oneToTen = list(range(10))
# An awesome thing about lists is that you can use many
# of the same functions with them that you used with strings

# Combine lists
randList = randList + oneToTen
print(randList)
# Get the 1st item with an index
print(randList[0])

# Get the length
print("List Length :", len(randList))
print("Last   item  :", randList[-1])
print("3 items before last :", randList[-4:-1])
# Slice a list to get 1st 3 items
first3 = randList[0:3]
# Cycle through the list and print the index
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# You can repeat a list item with *
print("first3[0] * 3 ( repeat a list item with '*')  = ", first3[0] * 3)

# You can see if a list contains an item
print("string" in first3)

# You can get the index of a matching item
print("Index of string :", first3.index("string"))

# Find out how many times an item is in the list
print("How many strings :", first3.count("string"))

# You can change a list item
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Append a value to the end of a list
first3.append("Another")

# ---------- PROBLEM : CREATE A RANDOM LIST ----------
# Generate a random list of 5 values between 1 and 9
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

# ---------- SORT A LIST : BUBBLE SORT ----------
# The Bubble sort is a way to sort a list
# It works this way
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of
#    the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning
#    of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at
#    the end of the list
# 7. Decrement the outer loop by 1

# Create the value that will decrement for the outer loop
# Its value is the last index in the list
i = len(numList) - 1

while i > 1:
    j  = 0
    while j < i:
        # Tracks the comparison of index values
        print("\nIs {} > {}".format(numList[j], numList[j + 1]))
        print()
        # If the value on the left is bigger switch values
        if numList[j] > numList[j + 1]:
            print("Switch")
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't Switch")
        j += 1

        for k in numList:  # Track changes to the list
            print(k)#, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

for k in numList:
    print(k)#, end=', ')
print()

# ---------- MORE LIST FUNCTIONS ----------
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

# Sort a list
numList.sort()

# Reverse a list
numList.reverse()

for k in numList:
    print(k)#, end=', ')
print()

# Insert value at index insert(index, value)
numList.insert(5, 10)

# Delete first occurrence of value
numList.remove(10)

for k in numList:
    print(k)#, end=", ")
print()

# Remove item at index
numList.pop(2)

for k in numList:
    print(k)#, end=", ")
print()
# ---------- LIST COMPREHENSIONS ----------
# You can construct lists in interesting ways using
# list comprehensions

# Perform an operation on each item in the list

# Create a list of even values
evenList = [i * 2 for i in range(10)]

for k in evenList:
    print(k)#, end=", ")
print()

# List of lists containing values to the power of
# 2, 3, 4
numList = [1, 2, 3, 4, 5]

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

# [[1.0, 1.0, 1.0], [4.0, 8.0, 16.0], [9.0, 27.0, 81.0], [16.0, 64.0, 256.0], [25.0, 125.0, 625.0]]
print("start list of  lists")
print(listOfValues)
print('end list of  lists')
print()
print("every list in a  line")
for k in listOfValues:
    print(k)
print()

# Create a 10 x 10 list
multiDList = [[0] * 10 for i in range(10)]

# Change a value in the multidimensional list
multiDList[0][1] = 10

# Get the 2nd item in the 1st list
# It may help to think of it as the 2nd item in the 1st row
print(multiDList[0][1])

# Get the 2nd item in the 2nd list
print(multiDList[1][1])

# ---------- MULTIDIMENSIONAL LIST ----------

# Show how indexes work with a multidimensional list
listTable = [[0] * 10 for i in range(10)]

for i in range(10):

    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):

    for j in range(10):
        print(listTable[i][j],  " || ")
    print()

# ---------- PROBLEM : CREATE MULTIPLICATION TABLE ----------
# With 2 for loops fill the cells in a multidimensional
# list with a multiplication table using values 1 - 9
'''
1, 2, 3, 4, 5, 6, 7, 8, 9,
2, 4, 6, 8, 10, 12, 14, 16, 18,
3, 6, 9, 12, 15, 18, 21, 24, 27,
4, 8, 12, 16, 20, 24, 28, 32, 36,
5, 10, 15, 20, 25, 30, 35, 40, 45,
6, 12, 18, 24, 30, 36, 42, 48, 54,
7, 14, 21, 28, 35, 42, 49, 56, 63,
8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81
'''

# Create the multidimensional list.   All values are 0
multTable = [[0] * 10 for i in range(10)]

# This will increment for each row
for i in range(1, 10):

    # This will increment for each item in the row
    for j in range(1, 10):
        # Assign the value to the cell
        multTable[i][j] = i * j

# Output the data in the same way you assigned it
for i in range(1, 10):

    for j in range(1, 10):
        print(multTable[i][j],  ", ")

    print()

    # 23:31
''' 
def format_list(L):
  return ", ".join(L[0::2]) + " and " + L[-1]

my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print( format_list(my_list) )

'''