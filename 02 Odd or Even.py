"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?
"""

check = int(input('Give me a number to check:'))
divby = int(input('Give me a number to divide by:'))


if check % divby == 0:
    print('{} is a multiple of {}.'.format(check, divby))
else:
    print('{} is not a multiple of {}.'.format(check, divby))
