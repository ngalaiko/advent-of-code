def part2(input):
    line = input.readline()
    line = line[:-1]
    for i in range(13, len(line)):
        if len(set(line[i-14:i])) == 14:
            return i


def part1(input):
    line = input.readline()
    line = line[:-1]
    for i in range(3, len(line)-3, 1):
        if len(set([line[i], line[i-1], line[i-2], line[i-3]])) == 4:
            return i+1


for file_name in ['example.txt', 'input.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
