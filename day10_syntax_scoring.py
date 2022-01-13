from queue import Empty


sample = ['[({(<(())[]>[[{[]{<()<>>',
          '[(()[<>])]({[<{<<[]>>(',
          '{([(<{}[<>[]}>{[]{[(<()>',
          '(((({<>}<{<{<>}{[]{[]{}',
          '[[<[([]))<([[{}[[()]]]',
          '[{[{({}]{}}([{[{{{}}([]',
          '{<[[]]>}<{[{[{[]{()[[[]',
          '[<(<(<(<{}))><([]([]()',
          '<{([([[(<>()){}]>(<<{{',
          '<{([{{}}[<[[[<>{}]]]>[]]']

def validate(input):
    
    close = ')}]>'
    check = '({[<'

    stack = []
    illegal = []

    for i in input:
        if i not in close:
            stack.append(i)
        else:
            if stack[-1] == check[close.index(i)]:
                stack.pop(-1)
            else:
                illegal.append(i)

    return [stack, illegal]

score = 0

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

for i in sample:
    result = validate(i)[1]
    print(validate(i)[0])
    print(validate(i)[1])

    print('')

    if len(result) > 0:
        for n in validate(i)[1]:
            score += points[n]
        
print(score)