# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fname = 'mbox-short.txt'
fh = open(fname)
summ = 0
lines = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    lines = lines + 1
    a = line.find('0.')
    b = line[a:]
    summ = summ + float(b)
avrg = summ/lines
print("Average spam confidence:", avrg)
