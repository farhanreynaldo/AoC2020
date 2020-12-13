with open("input/day03.txt", "r") as fn:
    day03 = [line.strip() for line in fn]


def traverse_tree(fields, right, down):
    x, y = 0, 0
    length, width = len(fields), len(fields[0])
    tree = 0
    while y < length:
        tree += day03[y][x % width] == "#"
        x += right
        y += down
    return tree


print(traverse_tree(day03, 3, 1))

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
answer = 1
for right, down in slopes:
    answer *= traverse_tree(day03, right, down)
print(answer)
