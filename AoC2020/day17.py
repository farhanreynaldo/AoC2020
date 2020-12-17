from itertools import product

SAMPLE = """
.#.
..#
###
"""


def neighbors3d(point):
    x, y, z = point
    dim = [[-1, 0, 1] for _ in range(3)]
    for dx, dy, dz in product(*dim):
        if (dx, dy, dz) != (0, 0, 0):
            yield x + dx, y + dy, z + dz


def neighbors4d(point):
    w, x, y, z = point
    dim = [[-1, 0, 1] for _ in range(4)]
    for dw, dx, dy, dz in product(*dim):
        if (dw, dx, dy, dz) != (0, 0, 0, 0):
            yield w + dw, x + dx, y + dy, z + dz


def parse_grid3d(raw):
    return {
        (x, y, 0)
        for y, line in enumerate(raw.strip().split("\n"))
        for x, p in enumerate(list(line))
        if p == "#"
    }


def parse_grid4d(raw):
    return {
        (0, x, y, 0)
        for y, line in enumerate(raw.strip().split("\n"))
        for x, p in enumerate(list(line))
        if p == "#"
    }


def next_grid(grid, dimension):
    opt = {3: neighbors3d, 4: neighbors4d}
    neighbors = opt[dimension]
    inactive_grid = {p for point in grid for p in neighbors(point) if p not in grid}
    new_grid = set()

    for point in grid:
        n = sum(p in grid for p in neighbors(point))
        if n in (2, 3):
            new_grid.add(point)

    for point in inactive_grid:
        n = sum(p in grid for p in neighbors(point))
        if n == 3:
            new_grid.add(point)

    return new_grid


def cycle(grid, num, dimension):
    for _ in range(num):
        grid = next_grid(grid, dimension)
    return len(grid)


grid3d = parse_grid3d(SAMPLE)
assert cycle(grid3d, 6, 3) == 112
day17 = open("input/day17.txt").read()
print(cycle(parse_grid3d(day17), 6, 3))

grid4d = parse_grid4d(SAMPLE)
assert cycle(grid4d, 6, 4) == 848
print(cycle(parse_grid4d(day17), 6, 4))
