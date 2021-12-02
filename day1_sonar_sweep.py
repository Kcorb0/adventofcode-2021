
from re import A


path = 'inputs/day1_input.txt'

file = open(path, 'r').readlines()

values = [int(i.replace('\n', '')) for i in file]

a = 0
b = 3

valsum = sum(values[a:b])
count = 0

while b != len(values):

    a += 1
    b += 1

    if sum(values[a:b]) > valsum:
        count += 1
    
    valsum = sum(values[a:b])

print(count)