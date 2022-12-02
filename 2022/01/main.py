def part2(input):
    by_elf = []
    curr = 0
    for line in input.readlines():
        line = line[:-1]
        if line == '':
            by_elf.append(curr)
            curr = 0
        else:
            curr += int(line)
    by_elf.append(curr)
    by_elf = sorted(by_elf, reverse=True)
    return by_elf[0]+by_elf[1]+by_elf[2]


def part1(input):
    res = 0
    curr = 0
    for line in input.readlines():
        line = line[:-1]
        if line == '':
            res = max(res, curr)
            curr = 0
        else:
            curr += int(line)
    by_elf.append(curr)
    return res


for file_name in ['example.txt', 'input.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
