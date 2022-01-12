path = 'inputs/day7_input.txt'
file = open(path, 'r').read().split(',')

file_nums = [int(i) for i in file]
# Input = List of horizontal positions of all crabs

test_nums = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

fuel_results = []

for hpos in range(2, 2000):
    results = []

    for num in file_nums:
        pos_change = hpos - num

        if pos_change < 0:
            pos_change *= -1
        
        results.append(pos_change*(pos_change+1)/2)

    fuel_results.append(sum(results))

print("Min Fuel: " + str(min(fuel_results)))