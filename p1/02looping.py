#!/usr/bin/env python3

import sys
print(sys.version)  
 
print("The Python version is %s.%s.%s" % sys.version_info[:3]) 

"""
#!/usr/bin/python
https://www.youtube.com/watch?v=swQEbZ6ez1I&index=2&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt
http://www.newthinktank.com/2016/06/learn-program-2/
"""
"""
for i in [2, 4, 6, 8, 10]:
    print("i = ", i)

# create a list starting at 0  - 9.
for i in range(10):
    print("i = ", i)

# We can define the starting and ending value for range
for i in range(2, 10):
    print("i = ", i)


i = 2
print((i % 2) == 0)  # Prints true
# PRINT ODDS FROM 1 to 20
for i in range(1, 21):
    if (i % 2) != 0:
        print("i = ", i)

# ---------- WORKING WITH FLOATS ----------
your_float = input("Enter a float: ")
# We can convert a string into a float like this
your_float = float(your_float)

# We can define how many decimals are printed being 2
# here by putting :.2 before f
print("Rounded to 2 decimals : {:.2f}".format(your_float))
"""
# 6:40  line 51

# ---------- PROBLEM : COMPOUNDING INTEREST ----------
# User enter their investment   and   interest
# Print earnings after  10 years
# Ask for money invested + the interest rate
"""
money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")

# Convert value to a float
money = float(money)

# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

# Cycle through 10 years using for and range from 0 to 9
for i in range(10):
    # Add the current money in the account + interest earned that year
    money = money + (money * interest_rate)
    print("year {} sum {}".format(i, money))

# Output the results
print("Investment after 10 years: {:.2f}".format(money))

"""

# ---------- WORKING WITH FLOATS ----------
# When working with floats understand that they are not precise
# This should print 0 but it doesn't
"""
i = 0.1 + 0.1 + 0.1 - 0.3
print(i)

# Floats will print nonsense beyond 16 digits of precision
i = .11111111111111111111111111111111
j = .00000000000000010000000000000001

print("Answer : {:.32}".format(i + j))
"""

# ---------- THE WHILE LOOP ----------
# We can use the random module to generate random numbers
import random
"""
# Generate a random integer between 1 and 50
rand_num = random.randrange(1, 51)

# The value we increment in the while loop is defined before the loop
i = 1

# Define the condition that while true we will continue looping
while (i != rand_num):
    # You must increment your iterator inside the while loop
    i += 1

# Outside of the while loop when we stop adding whitespace
print("The random value is : ", rand_num)

"""
# ---------- BREAK AND CONTINUE ----------
# Continue stops executing the code that remains in the loop and
# jumps back to the top

# Break jumps completely out of the loop

i = 1

while i <= 20:
    # If a number is even don't print it
    if (i % 2) == 0:
        i += 1
        continue
    # If i equals 15 stop looping
    if i == 15:
        break 
    # Print the odds
    print("Odd : ", i)
    # Increment i
    i += 1

# ---------- PROBLEM : DRAW A PINE TREE ----------
# For this problem I want you to draw a pine tree after asking the user
# for the number of rows. Here is the sample program

'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''

# You should use a while loop and 3 for loops

# I know that this is the number of spaces and hashes for the tree
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top

# So I need to
# 1. Decrement spaces by one each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash
# Get the number of rows for the tree
tree_height = input("How tall is the tree : ")

# Convert into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start that will be incremented
hashes = 1

# Save stump spaces til later
stump_spaces = tree_height - 1

# Makes sure the right number of rows are printed
while tree_height != 0:

    # Print the spaces
    # end="" means a newline won't be added
    for i in range(spaces):
        print(' ', end="")

    # Print the hashes
    for i in range(hashes):
        print('#', end="")

    print() # Newline after each row is printed

    # I know from research that spaces is decremented by 1 each time
    spaces -= 1

    # I know from research that hashes is incremented by 2 each time
    hashes += 2

    # Decrement tree height each time to jump out of loop
    tree_height -= 1

# Print the spaces before the stump and then a hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")