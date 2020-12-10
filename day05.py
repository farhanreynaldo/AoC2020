with open("input/day05.txt", "r") as fn:
    day05 = [line.strip() for line in fn]


def binary_split(code, symbols, low, high):
    if not code:
        return low
    lower_half, upper_half = symbols
    middle = (low + high) // 2
    if code[0] == lower_half:
        return binary_split(code[1:], symbols, low, middle)
    else:
        return binary_split(code[1:], symbols, middle + 1, high)


def seat_id_from(code):
    row_code, col_code = code[:7], code[7:]
    row_val = binary_split(row_code, "FB", 0, 127)
    col_val = binary_split(col_code, "LR", 0, 7)
    return row_val * 8 + col_val


assert seat_id_from("BFFFBBFRRR") == 567
assert seat_id_from("FFFBBBFRRR") == 119
assert seat_id_from("BBFFBBFRLL") == 820

print(max(seat_id_from(code) for code in day05))

seat_ids_current = list(seat_id_from(code) for code in day05)
seat_ids = list(range(min(seat_ids_current), max(seat_ids_current)))
print(set(seat_ids) - set(seat_ids_current))
