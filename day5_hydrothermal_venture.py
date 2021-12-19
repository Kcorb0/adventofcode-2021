path = 'inputs/day5_input.txt'
file = open(path, 'r').read().split('\n')

sorted_list = [i.split(" -> ") for i in file]

max_x = 1000
max_y = 1000

grid = []

for i in range(max_x):
    grid.append([0 for num in range(max_y)])

for coord in grid:
    print(coord)