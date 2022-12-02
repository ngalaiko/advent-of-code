def part2(input):
    shape = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}

    def lose(to):
        if to == 'A':
            return 'C'
        if to == 'B':
            return 'A'
        if to == 'C':
            return 'B'

    def win(to):
        if to == 'A':
            return 'B'
        if to == 'B':
            return 'C'
        if to == 'C':
            return 'A'

    def draw(to):
        return to

    total = 0
    for game in input.readlines():
        if len(game) == 0:
            continue

        if game[2] == 'X':
            total += 0 + shape[lose(game[0])]
        elif game[2] == 'Y':
            total += 3 + shape[draw(game[0])]
        elif game[2] == 'Z':
            total += 6 + shape[win(game[0])]

    return total


def part1(input):
    shape = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}
    outcome = {-1: 0, 0: 3, 1: 6}

    def play(opponent, me):
        if opponent == 'A':
            if me == 'X':
                return 3
            elif me == 'Y':
                return 6
            elif me == 'Z':
                return 0
        elif opponent == 'B':
            if me == 'X':
                return 0
            elif me == 'Y':
                return 3
            elif me == 'Z':
                return 6
        elif opponent == 'C':
            if me == 'X':
                return 6
            elif me == 'Y':
                return 0
            elif me == 'Z':
                return 3

    total = 0
    for game in input.readlines():
        if len(game) == 0:
            continue
        opponent = game[0]
        me = game[2]
        total += play(opponent, me) + shape[me]

    return total


for file_name in ['example.txt', 'input.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
