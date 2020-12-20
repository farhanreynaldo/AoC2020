from itertools import product

SAMPLE = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""


def parse_puzzle(raw):
    rules_raw, messages = raw.strip().split("\n\n")
    return rules_raw, messages


def parse_rules(raw):
    RULES, BASE = {}, {}
    for line in raw.strip().split("\n"):
        name, rule = line.split(": ")
        if rule.strip('"').isalpha():
            BASE[name] = [rule.strip('"')]
        else:
            RULES[name] = rule
    return RULES, BASE


def solve_rules(raw, check="0"):
    rules_raw, messages = parse_puzzle(raw)
    RULES, BASE = parse_rules(rules_raw)
    while len(BASE) - 2 < len(RULES):
        for rule, opt in RULES.items():
            digits = [item for item in opt.split() if item.isdigit()]
            if all(digit in BASE.keys() for digit in digits):
                possible_opt = []
                for exp in opt.split(" | "):
                    comb = [BASE[num] for num in exp.split()]
                    res = ["".join(item) for item in product(*comb)]
                    possible_opt += res
                BASE[rule] = possible_opt
    return sum(message in BASE[check] for message in messages.split("\n"))


assert solve_rules(SAMPLE) == 2

day19 = open("input/day19.txt").read()
# print(solve_rules(day19, '0'))


def test(s, seq):
    if s == "" or seq == []:
        return s == "" and seq == []  # if both are empty, True. If only one, False.

    r = rules[seq[0]]
    if '"' in r:
        if s[0] in r:
            return test(s[1:], seq[1:])  # strip first character
        else:
            return False  # wrong first character
    else:
        return any(test(s, t + seq[1:]) for t in r)  # expand first term


def parse_rule(s):
    n, e = s.split(": ")
    if '"' not in e:
        e = [[int(r) for r in t.split()] for t in e.split("|")]
    return (int(n), e)


rule_text, messages = [
    x.splitlines() for x in open("input/day19.txt").read().split("\n\n")
]
rules = dict(parse_rule(s) for s in rule_text)
print("Part 1:", sum(test(m, [0]) for m in messages))

rule_text += ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]
rules = dict(parse_rule(s) for s in rule_text)
print("Part 2:", sum(test(m, [0]) for m in messages))
