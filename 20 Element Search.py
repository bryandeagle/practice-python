"""
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number. The
function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.

Extras:
- Use binary search.
"""


def insert(ol, ti):
    for v in ol:
        if v > ti:
            ol.insert(v-1, ti)
            break
    return ol


print(insert([1, 2, 4, 5, 6, 7, 8, 9, 10], 3))
