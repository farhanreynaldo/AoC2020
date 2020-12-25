from collections import deque
from itertools import chain

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
    return "".join(str(cup) for cup in list(cups)[1:])


assert solve(SAMPLE, n=100) == "67384529"
day23 = "925176834"
print(solve(day23, n=100))


class Cup:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def create_cups(seq):
    cups = [None] * (1000000 + 1)
    start = (int(cup) for cup in list(seq))
    values = chain(start, range(10, 1000000 + 1))

    first = next(values)
    cups[first] = Cup(first)
    first = cups[first]
    prev = first

    for value in values:
        cur = cups[value] = Cup(value)
        cur.prev = prev
        prev.next = cur
        prev = cur
    cur.next = first

    return first, cups


def solve2(raw, n):
    cur, cups = create_cups(raw)
    maxcup = len(cups) - 1
    for _ in range(n):
        first = cur.next
        mid = first.next
        last = mid.next
        pickedup = (first.value, mid.value, last.value)

        cur.next = last.next
        last.next.prev = cur

        dest = maxcup if cur.value == 1 else cur.value - 1
        while dest in pickedup:
            dest = maxcup if dest == 1 else dest - 1

        dest = cups[dest]
        first.prev = dest
        last.next = dest.next
        dest.next.prev = last
        dest.next = first
        cur = cur.next

    return cups[1].next.value * cups[1].next.next.value


# assert solve2(SAMPLE, 10000000) == 149245887792
print(solve2(day23, 10000000))


# is changing object in list is changing list inplace?
