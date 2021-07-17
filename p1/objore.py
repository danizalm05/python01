# coding: utf-8
# !/usr/bin/env python3

import random
from urllib.request import urlopen # python 2.5 equivlant to 'from urllib import urlopen'
import sys

'''
In python3, urllib has been split into urllib.request and urllib.error. 
  
 
 page = urlopen("https://docs.python.org/3/howto/urllib2.html")
 contents = page.read()
 class — Tell Python to make a new kind of thing.
 object — Two meanings: the most basic kind of thing, and any instance of some thing.
 instance — What you get when you tell Python to create a class.
 def — How you define a function inside a class.
 self — Inside the functions in a class, self is a variable for the instance/object being accessed.
 inheritance — The concept that one class can inherit traits from another class, much like
         you and your parents.
 composition — The concept that a class can be composed of other classes as parts, much
         like how a car has wheels.
 attribute — A property classes have that are from composition and are usually variables.
 is- a — A phrase to say that something inherits from another, as in a “salmon” is- a “fish.”
 has- a — A phrase to say that something is composed of other things or has a trait, as in “a
         salmon has- a mouth.
'''
 
#  MODULES, CLASSES, AND OBJECTS  p. 142     'learn python the hard way'


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
            for line in self.lyrics:
                print (line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

'''
 
Why do I need self when I make __init__ or other functions for classes?

If you don’t have self, then code like cheese = 'Frank' is ambiguous. That code isn’t clear
about whether you mean the instance’s cheese attribute or a local variable named cheese. With
self.cheese = 'Frank' it’s very clear you mean the instance attribute self.cheese.
'''

# Learning to Speak Object Oriented  p. 146     'learn python the hard way'
#!/usr/bin/env python3

# ex41: Learning To Speak Object Oriented

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" # list of word to create
WORDS = []
'''
This program a test  for Learning to Speak Object Oriented
  
'''
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    print((word.strip().decode("utf-8")))

    WORDS.append(word.strip().decode("utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER:  %s\n\n" % answer)
except EOFError:
  print("\nBye")