# coding: utf-8
# !/usr/bin/env python3
# ex44d l 174: Learning To Speak Object Oriented
'''
Output  of this  program
PARENT implicit()
PARENT implicit()
PARENT override()
CHILD override()
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()

''' 
class Parent(object):
  def override(self):
     print ("PARENT override()")
  def implicit(self):
     print ("PARENT implicit()")
  def altered(self):
     print ("PARENT altered()")
 
class Child(Parent):
   def override(self):
        print ("CHILD override()")
   def altered(self):
        print ("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print ("CHILD, AFTER PARENT altered()")
dad = Parent()
son = Child()

dad.implicit()
son.implicit()
 
dad.override()
son.override()

dad.altered()
son.altered()