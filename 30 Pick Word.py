"""
In this exercise, the task is to write a function that picks a random word
from a list of words from the SOWPODS dictionary. Download this file and save
it in the same directory as your Python code. This file is Peter Norvig’s
compilation of the dictionary of words used in professional Scrabble
tournaments. Each line in the file contains a single word.
"""

from random import randrange


def get_word():
    with open('assets/sowpods.txt', 'rt') as f:
        words = [x.strip() for x in f.readlines()]
        return words[randrange(len(words))]


print(get_word())
