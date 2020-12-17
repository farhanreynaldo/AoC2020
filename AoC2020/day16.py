import re
from collections import defaultdict
from math import prod

SAMPLE = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""


def parse_tickets(ticket_raw):
    return [
        [int(n) for n in line.split(",")] for line in ticket_raw.strip().split("\n")[1:]
    ]


def parse_rules(rules_raw):
    name_rules = {}
    for line in rules_raw.strip().split("\n"):
        name, rule = line.split(": ")
        pat = r"(\d+)\-(\d+) or (\d+)\-(\d+)"
        ll, lu, ul, uu = re.search(pat, rule).groups()
        name_rules[name] = [range(int(ll), int(lu) + 1), range(int(ul), int(uu) + 1)]
    return name_rules


def is_valid(ticket, rule):
    return ticket in rule[0] or ticket in rule[1]


def error_rate(raw):
    rules_raw, ticket_raw, nearby_raw = raw.strip().split("\n\n")
    tickets, rules = parse_tickets(nearby_raw), parse_rules(rules_raw)
    return sum(
        ticket
        for row in tickets
        for ticket in row
        if not any(is_valid(ticket, rules[field]) for field in rules)
    )


assert error_rate(SAMPLE) == 71
day16 = open("input/day16.txt").read()
print(error_rate(day16))

def valid_tickets(tickets, rules):
    invalid_tickets = [
        line
        for line in tickets
        for ticket in line
        if not any(is_valid(ticket, rules[field]) for field in rules)
    ]
    return [line for line in tickets if line not in invalid_tickets]


def departure_value(raw):
    rules_raw, ticket_raw, nearby_raw = raw.strip().split("\n\n")
    my_ticket, nearby_tickets = parse_tickets(ticket_raw), parse_tickets(nearby_raw)
    rules = parse_rules(rules_raw)
    tickets = valid_tickets(my_ticket + nearby_tickets, rules)
    possible_fields = defaultdict(list)
    for col in range(len(tickets[0])):
        for field in rules.keys():
            if all(is_valid(line[col], rules[field]) for line in tickets):
                possible_fields[field].append(col)
    fields = defaultdict(int)

    # this is where if check valid field for each column
    while len(fields) < len(possible_fields):
        for field, cols in possible_fields.items():
            if len(cols) == 1:
                value = cols[0]
                fields[field] = value
                for field in possible_fields:
                    if value in possible_fields[field]:
                        possible_fields[field].remove(value)
    return prod(
        my_ticket[0][col] for field, col in fields.items() if "departure" in field
    )


print(departure_value(day16))
