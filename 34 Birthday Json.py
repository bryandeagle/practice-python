"""
In the previous exercise we created a dictionary of famous scientists’
birthdays. In this exercise, modify your program from Part 1 to load
the birthday dictionary from a JSON file on disk, rather than having the
dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to
the dictionary, and update the JSON file you have on disk with the scientist’s
name. If you run the program multiple times and keep adding new names, your
JSON file should keep getting bigger and bigger.
"""

import json

with open('assets/34.json', 'rt') as f:
    birthdays = json.loads(f.read())

lookup = input('Who\'s birthday do you want to look up?\n')
print('{}\'s birthday is {}'.format(lookup, birthdays[lookup]))
