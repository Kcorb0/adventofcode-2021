path = 'inputs/day9_input.txt'
file = open(path, 'r').read().split('\n')

# Risk level = 1 + Height

risk_sums = []

for idxr, row in enumerate(file):

    for idxc, col in enumerate(row):

        vecinity = []

        #check left
        if idxc > 0:
            vecinity.append(file[idxr][idxc-1])

        #check right
        if idxc < len(row)-1:
            vecinity.append(file[idxr][idxc+1])

        #check above
        if idxr > 0:
            vecinity.append(file[idxr-1][idxc])
        
        #check below
        if idxr < len(file)-1:
            vecinity.append(file[idxr+1][idxc])

        bottom = True
        for n in vecinity:
            if int(n) <= int(col):
                bottom = False
        
        if bottom == True:
            risk_sums.append(int(col)+1)

print(sum(risk_sums))


