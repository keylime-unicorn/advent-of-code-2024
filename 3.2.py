#!/usr/bin/python
import re

use_test = False
active = True

if use_test:
    file = open('3.test.txt', 'r')
else:
    file = open('3.txt', 'r')

multiply = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
deactivate = r'don\'t\(\)'
activate = r'do\(\)'
pattern = multiply + r'|' + deactivate + r'|' + activate

matches = []
for line in file.readlines():
    matches += re.findall(pattern, line)

total_sum = 0
for m in matches:
    if re.search(deactivate, m):
        active = False
    elif re.search(activate, m):
        active = True
    else: 
        if active:
            numbers = m.strip('mul()').split(',')
            total_sum += int(numbers[0])*int(numbers[1])

print(total_sum)