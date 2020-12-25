"""
http://devmag.org.za/2013/08/31/geometry-with-hex-coordinates
"""

from collections import Counter

SAMPLE = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

DIRECTION_MAP = dict(
    e=[1, 0, -1],
    w=[-1, 0, 1],
    se=[1, -1, 0],
    sw=[0, -1, 1],
    nw=[-1, 1, 0],
    ne=[0, 1, -1],
)


def parse_directions(line):
    directions = []
    twos = ["se", "sw", "nw", "ne"]
    i = 0
    while i < len(line):
        if line[i : i + 2] in twos:
            directions.append(line[i : i + 2])
            i += 2
        else:
            directions.append(line[i : i + 1])
            i += 1
    return directions


def parse_tiles(raw):
    return [parse_directions(line) for line in raw.strip().split("\n")]


def find_black_tiles(raw):
    tile_lines = parse_tiles(raw)
    tiles = Counter()
    for tile_line in tile_lines:
        coordinates = [DIRECTION_MAP.get(direction) for direction in tile_line]
        xs, ys, zs = zip(*coordinates)
        tile = (sum(xs), sum(ys), sum(zs))
        tiles[tile] += 1
    return {k: v for k, v in tiles.items() if v % 2 == 1}


def count_black(black_tiles):
    return len(black_tiles)


def neighbors(tile):
    x, y, z = tile
    for dx, dy, dz in DIRECTION_MAP.values():
        yield x + dx, y + dy, z + dz


def step(black_tiles):
    nbrs_tiles = Counter()
    for tile in black_tiles:
        for nbrs in neighbors(tile):
            nbrs_tiles[nbrs] += 1

    return {
        tile
        for tile, count in nbrs_tiles.items()
        if (tile in black_tiles and 1 <= count <= 2)
        or (tile not in black_tiles and count == 2)
    }


def art_exhibition(raw, n=5):
    black_tiles = find_black_tiles(raw)
    for _ in range(n):
        black_tiles = step(black_tiles)
    return black_tiles


assert count_black(find_black_tiles(SAMPLE)) == 10
day24 = open("input/day24.txt").read()
print(count_black(find_black_tiles(day24)))
assert count_black(art_exhibition(SAMPLE, 1)) == 15
assert count_black(art_exhibition(SAMPLE, 10)) == 37
print(count_black(art_exhibition(day24, 100)))
