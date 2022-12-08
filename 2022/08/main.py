def part2(input):
    matrix = parse_matrix(input)

    def count_top(matrix, i, j):
        if i == 0:
            return 0
        c = 0
        di = i - 1
        while di > 0 and matrix[i][j] > matrix[di][j]:
            c += 1
            di -= 1
        return c + 1

    def count_bottom(matrix, i, j):
        if i == len(matrix) - 1:
            return 0
        c = 0
        di = i+1
        while di < len(matrix)-1 and matrix[i][j] > matrix[di][j]:
            c += 1
            di += 1
        return c+1

    def count_left(matrix, i, j):
        if j == 0:
            return 0
        c = 0
        dj = j - 1
        while dj > 0 and matrix[i][j] > matrix[i][dj]:
            c += 1
            dj -= 1
        return c+1

    def count_right(matrix, i, j):
        if j == len(matrix[i])-1:
            return 0
        c = 0
        dj = j+1
        while dj < len(matrix[i])-1 and matrix[i][j] > matrix[i][dj]:
            c += 1
            dj += 1
        return c+1

    def score(matrix, i, j):
        return

    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            t = count_top(matrix, i, j)
            b = count_bottom(matrix, i, j)
            l = count_left(matrix, i, j)
            r = count_right(matrix, i, j)
            print(b, end=' ')
            c = max(t * b*l*r, c)
        print('')

    return c


def parse_matrix(input):
    matrix = []
    for line in input.readlines():
        row = []
        for char in line[:-1]:
            row.append(char)
        matrix.append(row)
    return matrix


def part1(input):
    matrix = parse_matrix(input)

    def is_visible_top(matrix, i, j):
        for di in range(i-1, -1, -1):
            if matrix[i][j] <= matrix[di][j]:
                return False
        return True

    def is_visible_bottom(matrix, i, j):
        for di in range(i+1, len(matrix), 1):
            if matrix[i][j] <= matrix[di][j]:
                return False
        return True

    def is_visible_left(matrix, i, j):
        for dj in range(j-1, -1, -1):
            if matrix[i][j] <= matrix[i][dj]:
                return False
        return True

    def is_visible_right(matrix, i, j):
        for dj in range(j+1, len(matrix[i]), 1):
            if matrix[i][j] <= matrix[i][dj]:
                return False
        return True

    def is_visible(matrix, i, j):
        return is_visible_top(matrix, i, j) or is_visible_bottom(matrix, i, j) or is_visible_left(matrix, i, j) or is_visible_right(matrix, i, j)

    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_visible(matrix, i, j):
                c += 1
    return c


for file_name in ['example.txt', 'input.txt']:
# for file_name in ['example.txt']:
    print(f'{file_name}:')
    with open(file_name) as file:
        print(f'    part1 {part1(file)}')
    with open(file_name) as file:
        print(f'    part2 {part2(file)}')
