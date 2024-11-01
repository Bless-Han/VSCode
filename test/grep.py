import re
fname = 'mbox.txt'
hand = open(fname)
pattern = input('Enter a regular expression: ')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(pattern, line): count += 1

print(f'{fname} had {count} lines that matched {pattern}')
