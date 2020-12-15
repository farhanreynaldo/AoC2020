from itertools import product


SAMPLE = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


def binary(num, pad=36):
    if isinstance(num, str):
        num = int(num)
    return format(num, f"0{pad}b")


def update_mem_val(value, mask):
    bin_val = binary(value)
    res = "".join(d if m == "X" else m for d, m in zip(bin_val, mask))
    return int(res, 2)


def program_init(raw):
    programs = {}
    for line in raw.split("\n"):
        kind, value = line.split(" = ")
        if line.startswith("mask"):
            programs[kind] = value
        else:
            kind = int("".join([i for i in kind if i.isdigit()]))
            new_val = update_mem_val(value, programs["mask"])
            programs[kind] = new_val
    return sum(value for key, value in programs.items() if key != "mask")


assert program_init(SAMPLE) == 165
day14 = open("input/day14.txt").read().strip()
print(program_init(day14))


def possible_memories(mem, mask):
    bin_val = binary(mem)
    res = ["X" if m == "X" else str(int(m) or int(d)) for d, m in zip(bin_val, mask)]
    x_idx = [i for i, val in enumerate(res) if val == "X"]
    memories = []
    for var in product(range(2), repeat=len(x_idx)):
        res_temp = res.copy()
        for x, val in zip(x_idx, var):
            res_temp[x] = str(val)
        memories.append(int("".join(res_temp), 2))
    return memories


def program_init2(raw):
    programs = {}
    for line in raw.split("\n"):
        kind, value = line.split(" = ")
        if line.startswith("mask"):
            programs[kind] = value
        else:
            kind = int("".join([i for i in kind if i.isdigit()]))
            memories = possible_memories(kind, programs["mask"])
            for mem in memories:
                programs[mem] = int(value)
    return sum(value for key, value in programs.items() if key != "mask")


SAMPLE2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

assert program_init2(SAMPLE2) == 208
print(program_init2(day14))
