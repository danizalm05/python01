#!/usr/bin/env python3
#
# More Practice ex 24   p84     'learn python the hard way'
'''
cd .git
ls -a | less      list hidden files scroll either up or down using 
the arrow keys 
or you can scroll down one page at a time with the space bar
     
rm -rf .<file-name/directory-name>  delete a single file or directory
'''       
from sys import argv
import sys
from os.path import exists
filename = 'ccc.txt'
py_ver =  sys.version_info.major
print ("/n/nYour python version is %d." % (py_ver))

print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
poem = """
 \tThe lovely world
  with logic so firmly planted
 cannot discern \n the needs of love
  nor comprehend passion from intuition
  and requires an explanation
  \n\t\twhere there is none.
  """
print ("- - - - - - - - - - - - - - ")
print (poem)
print ("- - - - - - - - - - - - - - ")


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(- 1)
    print (word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
  """Prints the first and last words of the sentence."""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# More Practice ex 24   p84     'learn python the hard way'


s = "All good things come to those who wait."
w = break_words(s)
print(w)
sorted_words = sort_words(w)
print(sorted_words)
print_first_word(w)
print_last_word(w)
sorted_words = sort_sentence(s)
print(sorted_words )
print(sorted_words[0])
#print_first_and_last(w)