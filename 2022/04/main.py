def part2(input):
    c = 0
    for line in input.readlines():
        line = line[:-1]
        parts = line.split(',')
        one_from = int(parts[0].split('-')[0])
        one_to = int(parts[0].split('-')[1])
        two_from = int(parts[1].split('-')[0])
        two_to = int(parts[1].split('-')[1])

        if one_from <= two_from <= one_to:
            c += 1
        elif one_from <= two_to <= one_to:
            c += 1
        elif two_from <= one_from <= two_to:
            c += 1
        elif two_from <= one_to <= two_to:
            c += 1

    return c


def part1(input):
    c = 0
    for line in input.readlines():
        line = line[:-1]
        parts = line.split(',')
        one_from = int(parts[0].split('-')[0])
        one_to = int(parts[0].split('-')[1])
        two_from = int(parts[1].split('-')[0])
        two_to = int(parts[1].split('-')[1])

        if one_from >= two_from and one_to <= two_to:
            c += 1
        elif two_from >= one_from and two_to <= one_to:
            c += 1

    return c


for file_name in ['example.txt', 'input.txt']:
    # for file_name in ['example.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
