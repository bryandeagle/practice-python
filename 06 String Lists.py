"""
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)
"""

string = input('Give me a string:').lower()

palindrome = True
for i in range(int(len(string)/2)):
    if string[i] != string[-i-1]:
        palindrome = False
        break

print({True: 'Palindrome', False: 'Not a Palindrome'}[palindrome])
