"""
For this exercise, we will keep track of when our friend’s birthdays are, and
be able to find that information based on their name. Create a dictionary
(in your file) of names and birthdays. When you run your program it should ask
the user to enter a name, and return the birthday of that person back to them.
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""

birthdays = {'Albert Einstein': '01/02/1900',
             'Benjamin Franklin': '02/03/1910',
             'Ada Lovelace': '03/04/1920'}

lookup = input('Who\'s birthday do you want to look up?\n')
print('{}\'s birthday is {}'.format(lookup, birthdays[lookup]))
