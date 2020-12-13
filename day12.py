from collections import defaultdict

SAMPLE = """F10
N3
F7
R90
F11"""


def solve(raw):
    instructions = [(e[0], int(e[1:])) for e in raw.split('\n')]
    x, y = 0, 0
    heading = 0 # East as 0, 90, 180, 270 for S, W, N respectively
    for action, value in instructions:
        if action == 'E':
            x += value
        elif action == 'S':
            y -= value
        elif action == 'W':
            x -= value
        elif action == 'N':
            y += value
        elif action == 'R':
            heading = (heading + value) % 360
        elif action == 'L':
            heading = (heading - value) % 360
        elif action == 'F':
            if heading == 0:
                x += value
            elif heading == 90:
                y -= value
            elif heading == 180:
                x -= value
            elif heading == 270:
                y += value
    return abs(x) + abs(y)

assert solve(SAMPLE) == 25
day12 = open('input/day12.txt').read()
print(solve(day12))

def solve2(raw):
    instructions = [(e[0], int(e[1:])) for e in raw.split('\n')]
    x, y = 0, 0
    wpx, wpy = 10, 1
    for action, value in instructions:
        if action == 'E':
            wpx += value
        elif action == 'S':
            wpy -= value
        elif action == 'W':
            wpx -= value
        elif action == 'N':
            wpy += value
        elif action == 'R':
            for _ in range(value // 90):
                wpx, wpy = wpy, -wpx
        elif action == 'L':
            for _ in range(value // 90):
                wpx, wpy = -wpy, wpx
        elif action == 'F':
            x += value * wpx
            y += value * wpy
    return abs(x) + abs(y)

assert solve2(SAMPLE) == 286
print(solve2(day12))