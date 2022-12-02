import math

def read_value(mode, mem, param):
    if mode == 0:
        return int(mem[param])
    elif mode == 1:
        return int(param)
    else:
        print('unknown mode', mode)

def parseCode(code):
    code = '00000' + code
    return int(code[len(code) - 1]), int(code[len(code) - 3]), int(code[len(code) - 4]), int(code[len(code) - 5])

def process(program):
    mem = program.split(',')
    mem = list(map(int, mem))

    i = 0
    while i < len(mem):
        code, m1, m2, m3 = parseCode(str(mem[i]))
        if code == 1:
            mem[mem[i+3]] = read_value(m1, mem, mem[i+1]) + read_value(m2, mem, mem[i+2])
            i+=4
        elif code == 2:
            mem[mem[i+3]] = read_value(m1, mem, mem[i+1]) * read_value(m2, mem, mem[i+2])
            i+=4
        elif code == 3:
            mem[mem[i+1]] = int(input('in:  '))
            i+=2
        elif code == 4:
            print('out:', read_value(m1, mem, mem[i+1]))
            i+=2
        elif code == 5:
            if read_value(m1, mem, mem[i+1]) != 0:
                i = read_value(m2, mem, mem[i+2])
            else:
                i+=3
        elif code == 6:
            if read_value(m1, mem, mem[i+1]) == 0:
                i = read_value(m2, mem, mem[i+2])
            else:
                i+=3
        elif code == 7:
            if read_value(m1, mem, mem[i+1]) < read_value(m2, mem, mem[i+2]):
                mem[mem[i+3]] = 1
            else:
                mem[mem[i+3]] = 0
            i+=4
        elif code == 8:
            if read_value(m1, mem, mem[i+1]) == read_value(m2, mem, mem[i+2]):
                mem[mem[i+3]] = 1
            else:
                mem[mem[i+3]] = 0
            i+=4
        elif code == 9:
            break
        elif code == 99:
            break
        else:
            print('invalid code')
    return mem

lines = [line.rstrip('\n') for line in open('./input.txt')]
for line in lines:
    mem = process(line)
