import random
randomlist = []
numbers = input("Enter amount of random numbers")
for i in range(0,int(numbers)):
    n = random.randint(1,10)
    randomlist.append(n)
print(randomlist)
