path = 'inputs/day3_input.txt'
file = open(path, 'r').read().split('\n')

grate = []
erate = []
cnt = 0

while cnt < len(file[0]):

    ls = [i[cnt] for i in file]
    
    if ls.count('1') > ls.count('0'):
        grate.append('1')
        erate.append('0')
    else:
        grate.append('0')
        erate.append('1')

    cnt += 1

dec_grate = int(''.join(grate), 2)
dec_erate = int(''.join(erate), 2)
print(f'Answer: {dec_grate*dec_erate}')

# Life support = o2 * Co2

