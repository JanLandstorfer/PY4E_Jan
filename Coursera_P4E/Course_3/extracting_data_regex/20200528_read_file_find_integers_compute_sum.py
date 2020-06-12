# import re
# f = open("regex_sum_517454.txt", "r")
#
# for line in f:
#     line=line.rstrip()
#     ints = re.findall('[0-9]+', line)
#     print(ints)



import re
# read file
f = open("regex_sum_517454.txt")
numlist = list()
for line in f:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    numlist.append(nums)
print(numlist)
# reduce list dimension from 2 to 1
flat_list = []
for sublist in numlist:
    for item in sublist:
        flat_list.append(int(item))
print('flat',flat_list)
# calculate total
total = 0
for i in flat_list:
    total = total + i
print(total)
