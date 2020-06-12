#fname = input("Enter file name: ")
fname = 'mbox-short.txt'
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
senders = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        m_addr = line.split()[1]
        senders[m_addr] = senders.get(m_addr, 0) + 1

count_sender = None
name_sender = None

for name, count in senders.items():
    if count_sender is None or count > count_sender:
        name_sender = name
        count_sender = count

print(name_sender, count_sender)