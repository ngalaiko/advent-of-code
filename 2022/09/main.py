import math


def part2(input):
    visited = set()
    rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
            (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

    def distance(head, tail):
        d = math.sqrt((head[0]-tail[0]) ** 2 + (head[1]-tail[1]) ** 2)
        return d

    def move(head, tail):
        d = distance(head, tail)
        if d >= 2:
            options = []
            for dx, dy in [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, -1), (1, -1), (-1, -1), (0, 1), (1, 1), (-1, 1)]:
                options.append((tail[0] + dx, tail[1] + dy))

            nt = tail
            for option in options:
                if distance(head, option) < distance(head, nt):
                    nt = option

            return nt
        else:
            return tail

    for line in input.readlines():
        line = line[:-1]
        direction = line[0]
        count = int(line[2:])

        for _ in range(count):
            if direction == 'U':
                rope[0] = (rope[0][0]+1, rope[0][1])
            elif direction == 'D':
                rope[0] = (rope[0][0]-1, rope[0][1])
            elif direction == 'L':
                rope[0] = (rope[0][0], rope[0][1]-1)
            elif direction == 'R':
                rope[0] = (rope[0][0], rope[0][1]+1)

            for i in range(1, len(rope)):
                rope[i] = move(rope[i-1], rope[i])

            visited.add(rope[-1])

    return len(visited)


def part1(input):
    visited = set()
    tail, head = (0, 0), (0, 0)

    def distance(head, tail):
        d = math.sqrt((head[0]-tail[0]) ** 2 + (head[1]-tail[1]) ** 2)
        return d

    def get_directions(direction):
        if direction == 'U':
            return [(1, 0), (1, 1), (1, -1)]
        elif direction == 'D':
            return [(-1, 0), (-1, 1), (-1, -1)]
        elif direction == 'L':
            return [(0, -1), (1, -1), (-1, -1)]
        elif direction == 'R':
            return [(0, 1), (1, 1), (-1, 1)]

    for line in input.readlines():
        line = line[:-1]
        direction = line[0]
        count = int(line[2:])

        for _ in range(count):
            if direction == 'U':
                head = (head[0]+1, head[1])
            elif direction == 'D':
                head = (head[0]-1, head[1])
            elif direction == 'L':
                head = (head[0], head[1]-1)
            elif direction == 'R':
                head = (head[0], head[1]+1)

            d = distance(head, tail)
            if d >= 2:
                options = []
                for dx, dy in get_directions(direction):
                    options.append((tail[0] + dx, tail[1] + dy))

                nt = tail
                for option in options:
                    if distance(head, option) < distance(head, nt):
                        nt = option

                tail = nt

            visited.add(tail)

    return len(visited)


for file_name in ['example.txt', 'input.txt']:
# for file_name in ['example.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
