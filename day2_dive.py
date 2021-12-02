
path = 'inputs/day2_input.txt'
file = open(path, 'r').read().split('\n')

horizontal = 0
depth = 0
aim = 0

for command in file:

    values = command.split(' ')
    direction = values[0]
    change = int(values[1])

    if direction == 'down':
        aim += change
    elif direction == 'up':
        aim -= change
    else:
        horizontal += change
        depth += (aim*change)


print('Answer: ' + str(horizontal*depth))