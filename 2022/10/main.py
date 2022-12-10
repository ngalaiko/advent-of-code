from collections import defaultdict


def parse_command(cmd):
    op = None
    args = []
    for part in cmd.split(' '):
        if len(part) > 0:
            if op is None:
                op = part
            else:
                args.append(part)
    return op, args


def part2(input):
    cycle = 1
    sprite = {}
    x = 1
    for line in input.readlines():
        op, args = parse_command(line[:-1])
        if op == 'noop':
            sprite[cycle] = x
            cycle += 1
            sprite[cycle] = x

        elif op == 'addx':
            sprite[cycle] = x
            cycle += 1
            sprite[cycle] = x

            cycle += 1
            x += int(args[0])
            sprite[cycle] = x

    cycle = 1
    for row in range(1, 7):
        for col in range(1, 41):
            if sprite[cycle] <= col <= sprite[cycle]+2:
                print('#', end='')
            else:
                print('.', end='')
            cycle += 1
        print('')


def part1(input):
    cycle = 1
    x = 1
    answer = 0
    for line in input.readlines():
        op, args = parse_command(line[:-1])
        if op == 'noop':
            cycle += 1
            if cycle % 40 == 20:
                answer += x * cycle

        elif op == 'addx':
            cycle += 1

            if cycle % 40 == 20:
                answer += x * cycle

            cycle += 1
            x += int(args[0])

            if cycle % 40 == 20:
                answer += x * cycle

    return answer


for file_name in ['example.txt', 'input.txt']:
# for file_name in ['example.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
