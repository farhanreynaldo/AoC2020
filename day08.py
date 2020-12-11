SAMPLE = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def parse_lines(raw):
    instructions = []
    for line in raw.strip().split("\n"):
        op, arg = line.split(" ")
        instructions.append((op, int(arg)))
    return instructions


def program(raw):
    lines = parse_lines(raw)
    current_index = 0
    visited_index = []
    acc = 0
    while current_index not in visited_index:
        visited_index.append(current_index)
        op, arg = lines[current_index]
        if op == "acc":
            acc += arg
            current_index += 1
        elif op == "jmp":
            current_index += arg
        else:
            current_index += 1
    return acc, visited_index


def get_acc(raw):
    acc, indices = program(raw)
    return acc

def change_ops(raw):
    flip_op = {'jmp': 'nop', 'nop': 'jmp'}
    lines = parse_lines(raw)
    prev_acc, indices = program(raw)
    allowed_indices = [index for index in indices if lines[index][0] in ['jmp', 'nop']]
    for allowed in allowed_indices[::-1]:
        current_index = 0
        visited_index = []
        acc = 0
        while current_index not in visited_index:
            if current_index == len(lines):
                return acc
            visited_index.append(current_index)
            op, arg = lines[current_index]
            op = flip_op[op] if current_index == allowed else op
            if op == "acc":
                acc += arg
                current_index += 1
            elif op == "jmp":
                current_index += arg
            else:
                current_index += 1


assert get_acc(SAMPLE) == 5
assert change_ops(SAMPLE) == 8

with open("input/day08.txt", "r") as fn:
    day08 = fn.read()

print(get_acc(day08))
print(change_ops(day08))
