#!/usr/bin/python

left = []
right = []
total = 0

file = open('1.txt', 'r')

for line in file.readlines():
    data = line.split()
    left.append(int(data[0]))
    right.append(int(data[1]))

left.sort()
right.sort()

for i in range(len(left)):
    diff = abs(left[i] - right[i])
    total += diff

print(total)