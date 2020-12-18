import re

SAMPLE = """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""
parens_pat = r'\([^()]*\)' # find most inner parentheses
add_pat = r'\d+ \+ \d+'

def evaluate(expression):
    items = expression.split(' ')
    value = int(items[0])
    for i in range(1, len(items), 2):
        op, next_value = items[i], int(items[i+1])
        if op == '+':
            value = value + next_value
        elif op == '*':
            value = value * next_value
    return value

def evaluate_same_precedence(raw):
    while '(' in raw or ')' in raw:
        exp = re.search(parens_pat, raw)
        exp_val = evaluate(exp.group()[1:-1])
        raw = raw[:exp.start()] + str(exp_val) + raw[exp.end():]
    return evaluate(raw)

def evaluate_higher_precedence(raw):
    while '(' in raw or ')' in raw:
        exp = re.search(parens_pat, raw)
        exp_val = evaluate_mult(exp.group()[1:-1])
        raw = raw[:exp.start()] + str(exp_val) + raw[exp.end():]
    return evaluate_mult(raw)

def evaluate_mult(raw):
    while '+' in raw:
        exp = re.search(add_pat, raw)
        exp_val = eval(exp.group())
        raw = raw[:exp.start()] + str(exp_val) + raw[exp.end():]
    return eval(raw)


assert evaluate_same_precedence('2 + 4 * 9') == 54
assert evaluate_same_precedence('2 * 3 + (4 * 5)') == 26
assert evaluate_same_precedence(SAMPLE) == 13632

day18 = open('input/day18.txt').read().split('\n')
print(sum(evaluate_same_precedence(line) for line in day18))

assert evaluate_higher_precedence('1 + 2 * 3 + 4 * 5 + 6') == 231
assert evaluate_higher_precedence('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340
print(sum(evaluate_higher_precedence(line) for line in day18))