fname = 'romeo.txt'
fh = open(fname)
counts = dict()

for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)
