from collections import Counter, defaultdict
from math import factorial


SAMPLE = """16
10
15
5
1
11
7
19
6
12
4"""

SAMPLE2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def difference(raw):
    numbers = sorted([0] + [int(num) for num in raw.strip().split("\n")])
    diff = [x - y for x, y in zip(numbers[1:], numbers)] + [3]
    return diff


def mult_one_three(raw):
    diff = Counter(difference(raw))
    return diff.get(1) * diff.get(3)


assert mult_one_three(SAMPLE) == 35
assert mult_one_three(SAMPLE2) == 220

day10 = open("input/day10.txt").read()
print(mult_one_three(day10))


def count_paths(raw):
    numbers = sorted([0] + [int(num) for num in raw.strip().split("\n")])

    numbers.append(max(numbers) + 3)

    paths = defaultdict(int)
    paths[0] = 1
    for number in numbers:
        for step in range(1, 4):
            next_number = number + step
            if next_number in numbers:
                paths[next_number] += paths[number]
    return paths[numbers[-1]]


assert count_paths(SAMPLE) == 8
assert count_paths(SAMPLE2) == 19208

print(count_paths(day10))
