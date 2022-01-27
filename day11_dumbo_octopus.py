path = 'inputs/day11_input.txt'
file = open(path, 'r').read().split('\n')

tfile = ['11111', '19991', '19191', '19991', '11111']

def detect_flashes(grid, steps=10):

    int_grid = [[int(col) for col in row] for row in grid]

    while steps > 0:
        
        for idxr, row in enumerate(int_grid):
            for idxc, col in enumerate(row):
                if col < 10:
                    int_grid[idxr][idxc] += 1
                if col >= 9:
                    int_grid[idxr][idxc] = 0
                
        
        steps -= 1

    return int_grid



for i in detect_flashes(tfile, 1):
    print(i)