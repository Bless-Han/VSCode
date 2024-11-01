fname = input('Enter a file name: ')
if len(fname) == 0:
    fname = 'frequency.txt'
fh = open(fname)

counts = dict()
total = 0
for line in fh:
    line = line.lower()
    for c in line:
        if c.isalpha():
            counts[c] = counts.get(c, 0) + 1
            total += 1

l = sorted([(v,k) for k,v in counts.items()], reverse=True)
for v,k in l:
    print(f'{k} {v} {v/total*100:.2f}%')
