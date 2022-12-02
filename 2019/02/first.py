import math

def process(program):
    mem = program.split(',')
    mem = list(map(int, mem))

    mem[1] = 12
    mem[2] = 2

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
    mem = process(line)
    print(mem)
