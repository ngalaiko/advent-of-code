def part2(input):
    sum = 0
    lines = input.readlines()
    for i in range(2, len(lines), 3):
        one, two, three = lines[i-2], lines[i-1], lines[i]
        intersect = set(one).intersection(
            set(two)).intersection(set(three))
        for char in list(intersect):
            if 'a' <= char <= 'z':
                # print(char, ord(char) - 96)
                sum += ord(char) - 96
            elif 'A' <= char <= 'Z':
                # print(char, ord(char) - 64+26)
                sum += ord(char) - 64+26
    return sum


def part1(input):
    sum = 0
    for line in input.readlines():
        line = line[:-1]
        middle = int(len(line)/2)
        left, right = line[:middle], line[middle:]
        intersect = set(left).intersection(set(right))
        if len(intersect) == 0:
            print(left, right)
            continue
        char = list(intersect)[0]
        if 'a' <= char <= 'z':
            # print(char, ord(char) - 96)
            sum += ord(char) - 96
        elif 'A' <= char <= 'Z':
            # print(char, ord(char) - 64+26)
            sum += ord(char) - 64+26
    return sum


for file_name in ['example.txt', 'input.txt']:
    # for file_name in ['example.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
