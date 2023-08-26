import random
import string

summary = {}

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    with open(file_name, 'w') as file:
        number = str(random.randint(1, 100))
        file.write(number)

        summary[file_name] = number

with open('summary.txt', 'w') as file:
    for file_name, number in summary.items():
        file.write(f'{file_name}: {number}\n')
