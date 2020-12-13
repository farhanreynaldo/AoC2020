from itertools import combinations

with open("input/day01.txt", "r") as fn:
    day01 = [int(line) for line in fn]

for i, j in combinations(day01, 2):
    if i + j == 2020:
        print(i * j)

for i, j, k in combinations(day01, 3):
    if i + j + k == 2020:
        print(i * j * k)
