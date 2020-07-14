"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:
1. Write two different functions to do this - one using a loop and constructing
   a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a
   different function.
"""


def dedup(arr):
    res = list()
    for i in arr:
        if i not in res:
            res.append(i)
    return res


print(dedup([1, 2, 3, 5, 2, 3, 8, 8, 9]))
