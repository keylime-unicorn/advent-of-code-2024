#!/usr/bin/python

left = []
right = {}
total = 0

file = open('1.txt', 'r')

for line in file.readlines():
    data = line.split()
    left.append(int(data[0]))
    if data[1] not in right.keys():
        right[data[1]] = 0
    right[data[1]] += 1

left.sort()

for location in left:
    try:
        total += location * right[str(location)]
    except:
        pass

print(total)