from collections import Counter

SAMPLE1 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

adjacents = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def parse_seats(raw):
    return [list(row) for row in raw.split("\n")]


def state(row, col, seats):
    rows, cols = len(seats), len(seats[0])
    count = Counter(
        seats[row + dr][col + dc]
        for dr, dc in adjacents
        if 0 <= row + dr < rows and 0 <= col + dc < cols
    )
    return (
        "#"
        if seats[row][col] == "L" and not count["#"]
        else "L"
        if seats[row][col] == "#" and count["#"] > 3
        else seats[row][col]
    )


def next_seats(seats):
    rows, cols = len(seats), len(seats[0])
    return [[state(row, col, seats) for col in range(cols)] for row in range(rows)]


def stable(raw):
    seats = parse_seats(raw)
    while True:
        if seats == next_seats(seats):
            break
        seats = next_seats(seats)
    rows, cols = len(seats), len(seats[0])
    return sum(seats[row][col] == "#" for row in range(rows) for col in range(cols))


def all_adjacents(row, col, dr, dc, seats):
    rows, cols = len(seats), len(seats[0])
    while True:
        row += dr
        col += dc
        if 0 <= row < rows and 0 <= col < cols:
            seat = seats[row][col]
            if seat in ['#', 'L']:
                return seat
        else:
            return '.'


def state2(row, col, seats):
    count = Counter(
        all_adjacents(row, col, dr, dc, seats)
        for dr, dc in adjacents
    )
    return (
        "#"
        if seats[row][col] == "L" and not count["#"]
        else "L"
        if seats[row][col] == "#" and count["#"] > 4
        else seats[row][col]
    )


def next_seats2(seats):
    rows, cols = len(seats), len(seats[0])
    return [[state2(row, col, seats) for col in range(cols)] for row in range(rows)]


def stable2(raw):
    seats = parse_seats(raw)
    while True:
        if seats == next_seats2(seats):
            break
        seats = next_seats2(seats)
    rows, cols = len(seats), len(seats[0])
    return sum(seats[row][col] == "#" for row in range(rows) for col in range(cols))


assert stable(SAMPLE1) == 37

day11 = open("input/day11.txt").read().strip()
print(stable(day11))

assert stable2(SAMPLE1) == 26
print(stable2(day11))