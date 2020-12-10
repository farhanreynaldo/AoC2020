with open("input/day02.txt", "r") as fn:
    day02 = [line.strip() for line in fn]

total = 0
for entry in day02:
    policy, password = entry.split(": ")
    rng, letter = policy.split(" ")
    low, high = rng.split("-")
    if int(low) <= password.count(letter) <= int(high):
        total += 1
print(total)

total = 0
for entry in day02:
    policy, password = entry.split(": ")
    rng, letter = policy.split(" ")
    low, high = rng.split("-")
    low_letter, high_letter = password[int(low) - 1], password[int(high) - 1]
    if low_letter == letter or high_letter == letter:
        if low_letter != high_letter:
            total += 1
print(total)
