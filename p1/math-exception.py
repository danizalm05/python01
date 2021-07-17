#!/usr/bin/env python3

import sys
print(sys.version)  
 
print("The Python version is %s.%s.%s" % sys.version_info[:3]) 

"""
#!/usr/bin/python
https://www.youtube.com/watch?v=02edODXdHgs&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=3
http://www.newthinktank.com/2016/06/learn-program-3/

 """

 # ---------- FORCE USER TO ENTER A NUMBER ----------
# By giving the while a value of True it will cycle until a break is reached
while True:
 
    # If we expect an error can occur surround potential error with try
    try:
        number = int(input("Please enter a number : "))
        break
 
    # The code in the except block provides an error message to set things right
    # We can either target a specific error like ValueError
    except ValueError:
        print("You didn't enter a number")
 
    # We can target all other errors with a default
    except:
        print("An unknown error occurred")
 
print("Thank you for entering a number")

# ---------- Problem : Implement a Do While Loop ----------
 
secret_number = 7
 
while True:
    guess = int(input("Guess a number between 1 and 10 : "))
 
    if guess == secret_number:
        print("You guessed it")
        break
# 6:04  line  51

# ---------- MATH MODULE ----------
# Python provides many functions with its Math module
import math
 
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))
print("factorial(4) = ", math.factorial(4))
 
# Return remainder of division
print("fmod(5,4) = ", math.fmod(5,4))
 
# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))
print("pow(2,2) = ", math.pow(2,2))
print("sqrt(4) = ", math.sqrt(4))
 
# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)
 
# Return e^x
# Return e^x
print("exp(4) = ", math.factorial(4))
 
# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))
 
# You can define the base and 10^3 = 1000
print("log(1000,10) = ", math.log(1000,10))
 
# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))
 
# We have the following trig functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh
 
# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))


# ---------- ACCURATE FLOATING POINT CALCULATIONS ----------
 
# The decimal module provides for more accurate floating point calculations
# With from you can reference methods without the need to reference the module
# like we had to do with math above
# We create an alias being D here to avoid conflicts with methods with
# the same name
from decimal import Decimal as D
 
sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
 
print("Sum = ", sum)
print(".1 + .1 +.1 - .3 = ",.1 + .1 +.1 - .3)

# 11:34  line  115