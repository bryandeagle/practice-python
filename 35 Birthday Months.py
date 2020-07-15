"""
In the previous exercise we saved information about famous scientists’ names
and birthdays to disk. In this exercise, load that JSON file from disk, extract
the months of all the birthdays, and count how many scientists have a birthday
in each month.

Your program should output something like:
{"May": 3, "November": 2, "December": 1}
"""
import json
from datetime import datetime

with open('assets/34.json', 'rt') as f:
    birthdays = json.loads(f.read())

counts = {}
for person in birthdays:
    month = datetime.strptime(birthdays[person], '%m/%d/%Y').strftime('%B')
    if month not in counts:
        counts[month] = 0
    counts[month] += 1
print(counts)
