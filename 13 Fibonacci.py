"""
Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about how you can use
functions. Make sure to ask the user to enter the number of numbers in the
sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


fibs = [1, 1]
amount = int(input('How many fibonacci numbers:'))
if amount == 1:
    print([1])
elif amount == 2:
    print(fibs)
else:
    for i in range(amount-2):
        fibs.append(fibs[-1] + fibs[-2])
    print(fibs)
