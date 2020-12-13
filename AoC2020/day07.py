import re
from collections import defaultdict

SAMPLE = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

with open("input/day07.txt", "r") as fn:
    day07 = fn.read()


def parse_lines(raw):
    bags = {}
    for line in raw.split('\n'):
        color, content = line.split(" contain ")
        color = color[:-5].strip()
        content = content.strip('.')
        if content == 'no other bags':
            bags[color] = {}
            continue
        subbags = {}
        for subbag in content.split(', '):
            num = int(subbag.split(' ')[0])
            subbag_color = ' '.join(subbag.split(' ')[1:-1])
            subbags[subbag_color] = num
        bags[color] = subbags
    return bags

def find_parents(bags):
    parents = defaultdict(list)
    for color in bags.keys():
        for item in bags[color].keys():
            parents[item].append(color)
    return parents

def is_contains(start, bags):
    parents = find_parents(bags)
    seen = set()
    stack = [start]

    while stack:
        color = stack.pop()
        for parent in parents.get(color, []):
            if parent not in seen:
                seen.add(parent)
                stack.append(parent)
    return list(seen)
        

assert len(is_contains('shiny gold', parse_lines(SAMPLE))) == 4
print(len(is_contains('shiny gold', parse_lines(day07))))

def count(color, bags):
    num = 0
    stack = [(color, 1)]
    while stack:
        next_color, multiplier = stack.pop()
        for item, count in bags[next_color].items():
            num += multiplier * count
            stack.append((item, multiplier * count))
    return num


assert count('shiny gold', parse_lines(SAMPLE)) == 32
print(count('shiny gold', parse_lines(day07)))
