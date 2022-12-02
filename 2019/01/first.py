import math

def calc(x):
    return math.floor(x / 3) - 2

lines = [line.rstrip('\n') for line in open('./input.txt')]
sum = 0
for line in lines:
    sum += calc(int(line))

print(sum)
