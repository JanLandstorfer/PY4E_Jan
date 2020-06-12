#fname = input("Enter file name: ")
fname = 'mbox-short.txt'
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        m_addr = line.split()[1]
        print(m_addr)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
