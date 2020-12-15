SAMPLE = """939
7,13,x,x,59,x,31,19"""


def earliest_depart(raw):
    depart_time, buses_raw = raw.split("\n")
    depart_time = start = int(depart_time)
    buses = [int(bus) for bus in buses_raw.split(",") if bus != "x"]
    while True:
        for bus in buses:
            if depart_time % bus == 0:
                return (depart_time - start) * bus
        depart_time += 1


assert earliest_depart(SAMPLE) == 295
day13 = open("input/day13.txt").read()
print(earliest_depart(day13))


def earliest_consecutive(raw):
    """
    The idea is we start from 0 with step 1.
    for each bus, after adding the number with step 1, 
    we will find the number with remainder 0. And then, 
    we multiply step by bus to make sure the number still
    divisible by previous bus, then proceed with each step
    """
    _, buses_raw = raw.split("\n")
    buses = [(i, int(bus)) for i, bus in enumerate(buses_raw.split(",")) if bus != "x"]
    start, step = 0, 1
    for i, bus in buses:
        while (start + i) % bus:
            start += step
        step *= bus
    return start


assert earliest_consecutive("0\n17,x,13,19") == 3417
assert earliest_consecutive("0\n67,7,59,61") == 754018
assert earliest_consecutive("0\n67,7,x,59,61") == 1261476
print(earliest_consecutive(day13))
