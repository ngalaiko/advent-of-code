import math

def process(program, pos1, pos2):
    mem = program.split(',')
    mem = list(map(int, mem))

    mem[1] = pos1
    mem[2] = pos2

    i = 0
    while i < len(mem):
        code = mem[i]
        if code == 1:
            mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
        elif code == 2:
            mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
        elif code == 99:
            break
        i+=4
    return mem

lines = [line.rstrip('\n') for line in open('./input.txt')]
for line in lines:
    for i in range(99):
        for j in range(99):
            mem = process(line, i, j)
            if mem[0] == 19690720:
                print(100 * i + j)
                exit(0)
