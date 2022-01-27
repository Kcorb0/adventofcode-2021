path = 'inputs/day4_input.txt'
file = open(path, 'r').read().split('\n\n')

# Run inputs for each card, output steps to first bingo


drawn = file[0].split(',')

def card_result(card, draws):
    new_card = sort_card(card)
    last_draw = None
    turns = 0
    
    for draw in draws:
        last_draw = draw
        turns += 1

        for row in range(len(new_card)):
            for col in range(len(new_card)):
                if new_card[row][col] == draw:
                    new_card[row][col] = 'x'

        if check_bingo(new_card) == 1:

            remaining_nums = []
            for rnums in new_card:
                remaining_nums.extend([int(rnum) for rnum in rnums if rnum != 'x'])

            return [turns, int(last_draw), sum(remaining_nums)]
                    
    return 'No bingo'


def sort_card(card):

    sorted_card = []
    for row in card.split('\n'):
        rem_spc = [i for i in row.split(' ') if i != '']
        sorted_card.append(rem_spc)

    return sorted_card

def check_bingo(card):

    for row in (card):
        if row.count('x') == 5:
            return 1
    for i in range(len(card)):
        if [num[i] for num in card].count('x') == 5:
            return 1

    return 0

winner = None

for card in file[1:]:
    
    if winner == None:
        winner = card_result(card, drawn)

    elif card_result(card, drawn)[0] > winner[0]:
        winner = card_result(card, drawn)

print(winner[1]*winner[2])
    