"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no
divisors.). You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

import math

num = int(input('Give me a number:'))

prime = True
for i in range(int(math.sqrt(num))):
    if num % (i+1) == 0:
        prime = False
        break

print({True: 'PRIME!', False: 'NOT PRIME!'}[prime])
