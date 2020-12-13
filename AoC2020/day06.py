from functools import reduce

with open("input/day06.txt", "r") as fn:
    day06 = fn.read()

SAMPLE = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def count_yes(data):
    total = 0
    for entry in data.split("\n\n"):
        total += len(set("".join(entry.split())))
    return total


assert count_yes(SAMPLE) == 11
print(count_yes(day06))


def count_unique_yes(data):
    total = 0
    for group in data.split("\n\n"):
        total += len(reduce(lambda a, b: set(a) & set(b), group.split()))
    return total


assert count_unique_yes(SAMPLE) == 6
print(count_unique_yes(day06))
