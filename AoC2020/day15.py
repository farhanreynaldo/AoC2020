from collections import defaultdict


def number_on(start, index=2020):
    num_index = defaultdict(list)
    numbers = []
    for i, num in enumerate(start):
        num_index[num].append(i)
        numbers.append(num)
    for i in range(len(start), index):
        prev = numbers[-1]
        if len(num_index[prev]) < 2:
            next_num = 0
        else:
            next_num = num_index[prev][-1] - num_index[prev][-2]
        numbers = numbers[-2:]
        numbers.append(next_num)
        num_index[next_num] = num_index[next_num][-2:]
        num_index[next_num].append(i)
    return numbers[-1]


assert number_on([1, 3, 2], 2020) == 1
assert number_on([2, 1, 3], 2020) == 10
assert number_on([1, 2, 3], 2020) == 27
assert number_on([2, 3, 1], 2020) == 78
assert number_on([3, 2, 1], 2020) == 438
assert number_on([3, 1, 2], 2020) == 1836
print(number_on([0, 13, 1, 8, 6, 15], 2020))
print(number_on([0, 13, 1, 8, 6, 15], 30000000))
