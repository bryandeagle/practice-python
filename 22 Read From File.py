"""
Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have a
.txt file for you, if you want to use it! (22.txt)
"""

with open('assets/22.txt', 'rt') as f:
    lines = f.readlines()

count = dict()
for name in lines:
    name = name.strip()
    if name not in count:
        count[name] = 0
    count[name] += 1

for name in count:
    print('Name: {}, Count; {}'.format(name, count[name]))
