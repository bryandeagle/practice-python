from datetime import datetime

# Get User Input
name = input("Enter your name:")
age = int(input("Enter your age:"))
num = int(input("Enter another number:"))

# Calculate result
year = datetime.today().year - age + 100

# Print result
print(num * 'Hello {}. You will turn 100 years old in {}.\n'.format(name, year))
