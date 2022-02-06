path = 'inputs/day13_input.txt'
file = open(path, 'r').read().split('\n\n')

points = [i.split(',') for i in file[0].split('\n')]

fold_coords = [c.replace('fold along ', '') for c in file[1].split('\n')]

max_x = max([int(i[0]) for i in points])
max_y = max([int(i[1]) for i in points])

print(max_x, max_y)

paper = [['.' for col in range(max_x+1)] for row in range(max_y+1)]

test_map = ['.']

def map_points(paper_map):

    for point in points:
        x = int(point[0])
        y = int(point[1])
    
        paper_map[y][x] = '#'

    for fold in fold_coords:
        ax = fold.split('=')[0]
        pos = int(fold.split('=')[1])

        if ax == 'x':
            left = [i[:pos] for i in paper_map]
            right = [i[pos+1:] for i in paper_map]

            for row in range(len(left)):
                for col in range(len(left[0])):
                    if right[row][-col] == '#':
                        left[row][col] == '#'
            
            return left


dots = 0

for i in map_points(paper):
    dots += i.count('#')

print(dots)