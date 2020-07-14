"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or
exactly right. (Hint: remember to use the user input lessons from the very
first exercise)

Extras:
1. Keep the game going until the user types “exit”
1. Keep track of how many guesses the user has taken,
   and when the game ends, print this out.
"""
import random

r = round(random.randrange(1, 9), 0)

count = 0
while True:
    g = int(input('Guess the number:'))
    count += 1
    if g < r:
        print('Too Low')
    elif g > r:
        print('Too High')
    else:
        print('Correct after {} guesses!'.format(count))
        break
