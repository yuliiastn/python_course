with open('lorem_ipsum.txt', 'w') as file1:
    file1.writelines(
        'Lorem ipsum dolor sit amet, '
        'consectetur adipiscing elit, sed do eiusmod '
        'tempor incididunt ut labore et dolore magna aliqua.'
        )

with open('lorem_ipsum.txt') as file1, open('lorem_copy.txt', 'w') as file2:
    line = file1.read()
    file2.write(line.upper())

    
