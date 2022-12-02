import math

def calc(x):
    return math.floor(x / 3) - 2

def smartCalc(x):
    total = 0
    while x >= 0:
        x = calc(x)
        if x >= 0:
            total += x
    return total

lines = [line.rstrip('\n') for line in open('./input.txt')]
sum = 0
for line in lines:
    sum += smartCalc(int(line))

print(sum)
