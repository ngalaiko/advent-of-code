def part2(input):
    rows = []
    nrows = 0
    ncols = 0
    stacks = []

    for line in input.readlines():
        line = line[:-1]
        if line == '':
            for j in range(ncols):
                stack = []
                stacks.append(stack)
                for i in range(nrows-1, -1, -1):
                    if rows[i][j] is not None:
                        stack.append(rows[i][j])
        elif line.startswith(' 1'):
            pass
        elif line.startswith('move'):
            parts = line.split(' ')
            count = int(parts[1])
            from_stack = int(parts[3])-1
            to_stack = int(parts[5])-1
            print(count, from_stack, to_stack)

            stacks[to_stack].extend(stacks[from_stack][-1*count:])
            stacks[from_stack] = stacks[from_stack][:-1*count]

            print('')
            for stack in stacks:
                if len(stack) > 0:
                    print(stack[-1])

        else:
            row = []
            rows.append(row)
            nrows += 1
            while len(line) > 0:
                cell = line[1:2]
                if cell != ' ':
                    row.append(cell)
                else:
                    row.append(None)
                ncols = max(ncols, len(row))
                line = line[4:]


def part1(input):
    rows = []
    nrows = 0
    ncols = 0
    stacks = []

    for line in input.readlines():
        line = line[:-1]
        if line == '':
            for j in range(ncols):
                stack = []
                stacks.append(stack)
                for i in range(nrows-1, -1, -1):
                    if rows[i][j] is not None:
                        stack.append(rows[i][j])
        elif line.startswith(' 1'):
            pass
        elif line.startswith('move'):
            parts = line.split(' ')
            count = int(parts[1])
            from_stack = int(parts[3])-1
            to_stack = int(parts[5])-1
            print(count, from_stack, to_stack)

            for _ in range(count):
                stacks[to_stack].append(stacks[from_stack][-1])
                stacks[from_stack] = stacks[from_stack][:-1]

            print('')
            for stack in stacks:
                if len(stack) > 0:
                    print(stack[-1])

        else:
            row = []
            rows.append(row)
            nrows += 1
            while len(line) > 0:
                cell = line[1:2]
                if cell != ' ':
                    row.append(cell)
                else:
                    row.append(None)
                ncols = max(ncols, len(row))
                line = line[4:]


for file_name in ['example.txt', 'input.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
