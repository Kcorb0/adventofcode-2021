
path = 'inputs/day1_input.txt'

file = open(path, 'r').read().split('\n')

count = 0

cur_num = file[0]

for i in file:
    
    if i > cur_num:
        count += 1
    
    cur_num = i

print(count)
