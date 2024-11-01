import string

fname = input('Enter a file name: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)

counts = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) >= 6 and words[0] == 'From':
        hour = words[5].split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

for hour,count in sorted(counts.items()):
    print(hour, count)

