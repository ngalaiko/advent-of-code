import math

def process(line1, line2):
    field = []
    side = 400
    for i in range(side):
        line = []
        for j in range(side):
            line.append('')
        field.append(line)

    print('sdasd')

    len = int(side / 2)

    draw(line1, field, [len,len])
    points = draw(line2, field, [len,len])

    min = len
    for p in points:
        dist = abs(p[1]-len) + abs(p[0]-len)
        if dist < min:
            min = dist

    return min

def draw(line, field, pos):
    point = []
    for step in line:
        dist = int(step[1:])
        if step[0] == 'R':
            for i in range(dist):
                pos[1] += 1
                if field[pos[0]][pos[1]] == '*':
                    point.append([pos[0], pos[1]])
                field[pos[0]][pos[1]] = '*'
        elif step[0] == 'L':
            for i in range(dist):
                pos[1] -= 1
                if field[pos[0]][pos[1]] == '*':
                    point.append([pos[0], pos[1]])
                field[pos[0]][pos[1]] = '*'
        elif step[0] == 'U':
            for i in range(dist):
                pos[0] += 1
                if field[pos[0]][pos[1]] == '*':
                    point.append([pos[0], pos[1]])
                field[pos[0]][pos[1]] = '*'
        elif step[0] == 'D':
            for i in range(dist):
                pos[0] -= 1
                if field[pos[0]][pos[1]] == '*':
                    point.append([pos[0], pos[1]])
                field[pos[0]][pos[1]] = '*'
    return point

lines = [line.rstrip('\n') for line in open('./input.txt')]

print(process(lines[0].split(','), lines[1].split(',')))
