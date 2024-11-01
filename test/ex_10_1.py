import string

fname = input('Enter a file name: ')
if len(fname) == 0: fh = open('mbox-short.txt')
else: fh = open(fname)

counts = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) >=2 and words[0] == 'From':
        counts[words[1]] = counts.get(words[1], 0) + 1

count, address = sorted([(v,k) for k,v in counts.items()], reverse=True)[0]
print(address, count)

