"""
Given two .txt files that have lists of numbers in them, find the numbers that
are overlapping. One .txt file has a list of all prime numbers under 1000, and
the other .txt file has a list of happy numbers up to 1000.
"""

with open('assets/primenumbers.txt', 'rt') as p:
    prime = set([x.strip() for x in p.readlines()])

with open('assets/happynumbers.txt', 'rt') as h:
    happy = set([x.strip() for x in h.readlines()])

print(list(prime.intersection(happy)))
