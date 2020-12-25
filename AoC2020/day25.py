def find_loop_size(public_key, subject_number=7):
    loop_size, value = 1, 1
    while True:
        value = (value * subject_number) % 20201227
        if value == public_key:
            break
        loop_size += 1
    return loop_size


def find_encryption_key(card_key, door_key):
    """
    you can switch card key and door key and still yield
    the same result
    """
    loop_size = find_loop_size(card_key)
    value = 1
    for _ in range(loop_size):
        value = (value * door_key) % 20201227
    return value


assert find_loop_size(5764801) == 8
assert find_loop_size(17807724) == 11
assert find_encryption_key(5764801, 17807724) == 14897079

card_key, door_key = [int(key) for key in open("input/day25.txt").read().split("\n")]
print(find_encryption_key(card_key, door_key))
