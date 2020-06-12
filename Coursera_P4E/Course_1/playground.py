numbers = [3,6,1,2,3]
nnumbers = numbers
count = 0
for n in nnumbers:
    for i in numbers:
        index = int(nnumbers[n])
        if i == numbers[index]:
            count = count + 1
    print(count)
