from collections import deque

SAMPLE = "389125467"

def solve(seq, n=10):
    cups = deque(int(cup) for cup in list(seq))
    low, high = min(cups), max(cups)
    
    for _ in range(n):
        current = cups[0]
        cups.rotate(-1)
        pickup = []
        for _ in range(3):
            pickup.append(cups.popleft())
        dest = current - 1
        if dest < low:
            dest = high
        while dest in pickup:
            dest -= 1
            if dest < low:
                dest = high

        while dest != cups[0]:
            cups.rotate(-1)
        cups.rotate(-1)
        cups.extend(pickup)

        while current != cups[0]:
            cups.rotate(-1)
        cups.rotate(-1)
    while cups[0] != 1:
        cups.rotate(-1)
    return ''.join(str(cup) for cup in list(cups)[1:])

assert solve(SAMPLE, n=100) == '67384529'
day23 = '925176834'
print(solve(day23, n=100))

def solve_million(seq, n=1_000_000):
    cups = deque(int(cup) for cup in list(seq) + list(range(10, 1_000_000)))
    low, high = min(cups), max(cups)
    
    for _ in range(n):
        if _ % 100 == 0:
            print(_)
        current = cups[0]
        cups.rotate(-1)
        pickup = []
        for _ in range(3):
            pickup.append(cups.popleft())
        dest = current - 1
        if dest < low:
            dest = high
        while dest in pickup:
            dest -= 1
            if dest < low:
                dest = high

        while dest != cups[0]:
            cups.rotate(-1)
        cups.rotate(-1)
        cups.extend(pickup)

        while current != cups[0]:
            cups.rotate(-1)
        cups.rotate(-1)
    while cups[0] != 1:
        cups.rotate(-1)
    return ''.join(str(cup) for cup in list(cups)[1:])

print(solve_million(day23))