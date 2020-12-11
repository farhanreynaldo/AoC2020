from itertools import combinations
from collections import deque

SAMPLE = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

sample_num = [int(num) for num in SAMPLE.strip().split("\n")]


def weakness(numbers, window=25, return_index=False):
    for i in range(len(numbers[window:]) - window):
        preamble, target = numbers[i : i + window], numbers[i + window]
        if target not in [x + y for x, y in combinations(preamble, 2)]:
            return (target, i + window) if return_index else target


assert weakness(sample_num, 5) == 127

day09 = [int(num) for num in open("input/day09.txt").read().split("\n")]
print(weakness(day09, 25))


def contiguous_set(numbers, window=25):
    target, weakness_index = weakness(numbers, window, True)
    i = 0
    while i < weakness_index:
        j = i + 1
        while j < weakness_index:
            if sum(numbers[i:j]) == target:
                return max(numbers[i:j]) + min(numbers[i:j])
            elif sum(numbers[i:j]) > target:
                j = weakness_index
            j += 1
        i += 1

assert contiguous_set(sample_num, 5) == 62
print(contiguous_set(day09, 25))