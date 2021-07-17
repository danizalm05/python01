#!/usr/bin/env python3
# https://www.youtube.com/watch?v=1Xa_iDqvg94
# http://www.newthinktank.com/2016/07/learn-program-5/
def add (num_1, num2):
	  return num_1 + num2
 
 

# ---------- EXAMPLE 4 ----------
# You can also use the global statement to change it
gbl_name = "Sally"

 
def change_name_3():
	global gbl_name
	gbl_name = "Sammy"

change_name_3()
print(gbl_name)


# ---------- PROBLEM : SOLVE FOR X ----------
# Make a function that receives an algebraic equation like
# x + 4 = 9 and solve for x
# x will always be the 1st value received and you only
# will deal with addition

# Receive the string and split the string into variables
def solve_eq(equation):
	x, add, num1, equal, num2 = equation.split()
	# Convert the strings into ints
	num1, num2 = int(num1), int(num2)
	# Convert the result into a string and join (concatenate)
	# it to the string "x = "
	return "x = " + str(num2 - num1)


print(solve_eq("x + 4 = 9"))


# ---------- RETURN MULTIPLE VALUES ----------
# You can return multiple values with the return statement

def mult_divide(num1, num2):
	return (num1 * num2), (num1 / num2)


mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)


# ---------- RETURN A LIST OF PRIMES ----------
# A prime can only be divided by 1 and itself
# 6 is a composite because it is divisible by 1, 2, 3 and 6

# We'll receive a request for primes up to the input value
# We'll then use a for loop and check if modulus == 0 for
# every value up to the number to check
# If modulus == 0 that means the number isn't prime

def isprime(num):
	# This for loop cycles through primes from 2 to
	# the value to check
	for i in range(2, num):

		# If any division has no remainder we know it
		# isn't a prime number
		if (num % i) == 0:
			return False
	return True


def getPrimes(max_number):
	# Create a list to hold primes
	list_of_primes = []

	# This for loop cycles through primes from 2 to
	# the maximum value requested
	for num1 in range(2, max_number):

		if isprime(num1):
			list_of_primes.append(num1)

	return list_of_primes


max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
	print(prime)
# 159   19:29

# ---------- UNKNOWN NUMBER OF ARGUMENTS ----------
# We can receive an unknown number of arguments using
# the splat (*) operator

def sumAll(*args):
	sum = 0

	for i in args:
		sum += i

	return sum

print("Sum :", sumAll(1, 2, 3, 4))

import math


def get_area(shape):
	# Switch to lowercase for easy comparison
	shape = shape.lower()

	if shape == "rectangle":
		rectangle_area()
	elif shape == "circle":
		circle_area()
	else:
		print("Please enter rectangle or circle")


# Create function that calculates the rectangle area
def rectangle_area():
	length = float(input("Enter the length : "))
	width = float(input("Enter the width : "))

	area = length * width

	print("The area of the rectangle is", area)


# Create function that calculates the circle area
def circle_area():
	radius = float(input("Enter the radius : "))

	area = math.pi * (math.pow(radius, 2))

	# Format the output to 2 decimal places
	print("The area of the circle is {:.2f}".format(area))


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
  
  
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

def print_all(f):

    print (f.read())

def main():

    print_two_again("Zed","Shaw")
    #functions and files page 74 'python the hard way'
    input_file = 'ccc.txt'
    current_file = open(input_file)
    print("First let's print the whole file:\n")
    print_all(current_file)
    age = add(30, 5)
    print   ("Age: %d " % (age ))
	#Learn   python  the  hard way p 78 ex21 
	#Functions Can Return Something
	
	
	
main()