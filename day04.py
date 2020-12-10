import re

with open("input/day04.txt", "r") as fn:
    content = [entry.split() for entry in fn.read().split("\n\n")]
    passports = []
    for passport in content:
        fields = {}
        for field in passport:
            key, value = field.split(":")
            fields[key] = value
        passports.append(fields)

fields = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (
        "cm" in x and 150 <= int(x[:-2]) <= 193 or "in" in x and 59 <= int(x[:-2]) <= 76
    ),
    "ecl": lambda x: x in "amb blu brn gry grn hzl oth".split(),
    "hcl": lambda x: re.fullmatch(r"^#[0-9a-f]{6}$", x),
    "pid": lambda x: re.fullmatch(r"\d{9}", x),
}

valid = 0
for passport in passports:
    valid += all([field in passport.keys() for field in fields.keys()])
print(valid)

valid = 0
for passport in passports:
    if not all([field in passport.keys() for field in fields.keys()]):
        continue
    valid += all([func(passport[field]) for field, func in fields.items()])
print(valid)
