path = 'inputs/day6_input.txt'
file = open(path, 'r').read()

test_sample = [3,4,3,1,2]
sample = [int(num) for num in file.split(',')]

# Notes
# Exponential growth
# New lfish every 7 days

# Part 1
def growth_sim(sample, duration):

    new_sample = sample

    while duration > 0:
        for i in range(len(new_sample)):

            if new_sample[i] == 0:
                new_sample[i] = 6
                new_sample.append(8)
            else:
                new_sample[i] -= 1
        
        duration -= 1

    return len(new_sample)


# Part 2
def growth_sim_2(sample, duration):

    new_sample = {}

    for i in range(9):
        if i not in sample:
            new_sample[i] = 0
        else:
            new_sample[i] = sample.count(i)

    print(new_sample)
    while duration > 0:

        if new_sample[0] > 0:
            new_sample[8] += new_sample[0]
            new_sample[6] += new_sample[0]

        for x in range(0, 8):
            
            val = new_sample[x]
            new_sample[x] += new_sample[x+1]
            new_sample[x] -= val
        
        print(new_sample)
            
        
        duration -= 1

    return new_sample

#print(growth_sim(test_sample, 20))
growth_sim_2(test_sample, 4)