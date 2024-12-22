#!/usr/bin/python
import re

use_test = False

if use_test:
    file = open('3.test.txt', 'r')
else:
    file = open('3.txt', 'r')


pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'

matches = []
for line in file.readlines():
    matches += re.findall(pattern, line)

total_sum = 0
for m in matches:
    numbers = m.strip('mul()').split(',')
    total_sum += int(numbers[0])*int(numbers[1])

print(total_sum)