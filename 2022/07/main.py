def part2(input):
    tree = parse_tree(input)

    sizes = []

    def size(tree):
        s = 0
        for name, object in tree.items():
            if type(object) == int:
                s += object
            else:
                sz = size(object)

                sizes.append(sz)

                s += sz
        return s

    total = size(tree)
    free = 70000000 - total
    for s in sorted(sizes):
        if free + s > 30000000:
            return s
    return None


def parse_tree(input):
    fs = {}
    stack = [fs]
    for line in input.readlines():
        line = line[:-1]

        if line.startswith('$'):
            parts = line[2:].split(' ')
            cmd = parts[0]
            args = parts[1:]
            if cmd == 'ls':
                pass
            elif cmd == 'cd':
                if args[0] == '/':
                    stack = stack[:1]
                elif args[0] == '..':
                    stack.pop(-1)
                else:
                    stack.append(stack[-1][args[0]])
            else:
                raise Exception(f'unknown command {cmd}')
        else:
            if line.startswith('dir'):
                name = line.split(' ')[1]
                stack[-1][name] = {}
            else:
                parts = line.split(' ')
                name = parts[1]
                size = parts[0]
                stack[-1][name] = int(size)
    return fs


def part1(input):
    tree = parse_tree(input)

    m = []

    def size(tree):
        s = 0
        for name, object in tree.items():
            if type(object) == int:
                s += object
            else:
                sz = size(object)

                if sz < 100000:
                    m.append(sz)

                s += sz
        return s

    size(tree)
    s = 0
    for ss in m:
        s += ss
    return s


for file_name in ['example.txt', 'input.txt']:
    # for file_name in ['example.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
