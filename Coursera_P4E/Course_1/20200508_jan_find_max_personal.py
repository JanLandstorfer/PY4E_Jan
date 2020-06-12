import random
randomlist = []
numbers = input("Enter amount of random numbers: ")
for i in range(0,int(numbers)):
    n = random.randint(0,99)
    randomlist.append(n)
#print(randomlist)

maxv = 0
minv = 300
count = 0
maxcount = 0
mincount = 0

for i in randomlist:
    if i < minv:
        minv = i
    count = count + 1
    if i > maxv:
        maxv = i
print("Max Value =", maxv)
print("Min Value =", minv)
print("Total numbers count =", count)

for i in randomlist:
    if i == maxv:
        maxcount = maxcount + 1
    if i == minv:
        mincount = mincount + 1

print ("Maxcount =", maxcount)
print("Min Count =", mincount)
