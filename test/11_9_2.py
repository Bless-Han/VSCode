import re
fname = input('Enter a file name: ')
fhand = open(fname)
lst = list()
for line in fhand:
    line = line.rstrip()
    rev = re.findall('New Revision: ([0-9]+)$', line)
    if len(rev) > 0:
        lst.append(int(rev[0]))

print(int(sum(lst) / len(lst)))

