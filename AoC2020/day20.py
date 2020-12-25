from itertools import combinations, product
from collections import defaultdict
from math import prod

SAMPLE = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile

    def rotate(self, n=1):
        rotated_tile = self.tile
        for _ in range(n):
            self.tile = [list(row) for row in zip(*reversed(rotated_tile))]
        return self

    def flip(self, vertical=False):
        if vertical:
            self.tile = [list(reversed(row) for row in self.tile)]
        self.tile = list(reversed(self.tile))
        return self

    def configurations(self):
        for vertical in [True, False]:
            for n in [0, 1, 2, 3]:
                yield self.flip(vertical).rotate(n)

    def __repr__(self):
        return f"Tile ID: {self.id}"

    def side(self, name):
        sides = {
            "top": self.tile[0],
            "right": [row[0] for row in self.tile],
            "bottom": self.tile[-1],
            "left": [row[-1] for row in self.tile],
        }
        return sides.get(name)

    @property
    def edges(self):
        # return [self.top, self.right, self.bottom, self.left]
        return [self.side(name) for name in ["top", "right", "bottom", "left"]]


def parse_tiles(raw):
    tiles = []
    for tile_raw in raw.strip().split("\n\n"):
        tile_id, *tile = tile_raw.split("\n")
        tile_id = int(tile_id[5:-1])
        tile = [list(row) for row in tile]
        tiles.append(Tile(tile_id, tile))
    return tiles


def find_corners(raw):
    """
    Corner should only have 2 edges match with
    other tile edges
    """
    SIDES = ["top", "right", "bottom", "left"]
    tiles_matches = defaultdict(set)
    tiles = parse_tiles(raw)
    for tile1, tile2 in combinations(tiles, 2):
        for pos1, pos2 in product(SIDES, SIDES):
            edge1, edge2 = tile1.side(pos1), tile2.side(pos2)
            if edge1 == edge2 or edge1 == edge2[::-1]:
                tiles_matches[tile1.id].add(pos1)
                tiles_matches[tile2.id].add(pos2)
    return {tile: sides for tile, sides in tiles_matches.items() if len(sides) == 2}


def multiply_corner_id(raw):
    return prod(tile for tile in find_corners(raw))


assert multiply_corner_id(SAMPLE) == 20899048083289
day20 = open("input/day20.txt").read()
print(multiply_corner_id(day20))
