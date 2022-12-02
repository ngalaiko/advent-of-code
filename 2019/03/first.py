import math

def sort(aa):
    if aa[0] > aa[1]:
        return aa
    return [aa[1], aa[0]]

def start(l):
    return l[0]

def end(l):
    return l[1]

def x(l):
    return l[0]

def y(l):
    return l[1]

def intersect(l1, l2):
    return None

def process(line1, line2):
    lines1 = get_lines(line1, [0,0])
    lines2 = get_lines(line2, [0,0])

    dist = 1000000000
    for l1 in lines1:
        for l2 in lines2:
            p = intersect(l1, l2)
            if p == None:
                continue

            print(p[0] + p[1])

    return ''

def get_lines(paths, pos):
    ll = []
    for step in paths:
        l = []
        l.append([pos[0], pos[1]])
        dist = int(step[1:])
        if step[0] == 'R':
            pos[1] += dist
        elif step[0] == 'L':
            pos[1] -= dist
        elif step[0] == 'U':
            pos[0] += dist
        elif step[0] == 'D':
            pos[0] -= dist
        l.append([pos[0], pos[1]])
        ll.append(l)
    return ll

lines = [line.rstrip('\n') for line in open('./input.txt')]

print(process(lines[0].split(','), lines[1].split(',')))
