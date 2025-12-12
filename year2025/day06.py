import math


def parse_input(data: str):
    lines = data.splitlines(keepends=True)
    return lines


def calculate(nums: list[int], op: str) -> int:
    return sum(nums) if op == "+" else math.prod(nums)


def part1(lines: list[str]) -> int:
    rows = [line.split() for line in lines]
    problems: list[list[str]] = list(map(list, zip(*rows)))
    total = 0

    for p in problems:
        *digits, op = p
        nums = list(map(int, digits))
        total += calculate(nums, op)

    return total


def part2(lines: list[str]) -> int:
    rows = [line.strip("\n") for line in lines]
    cols: list[tuple[str]] = list(zip(*rows))
    total = 0

    groups: list[list[tuple[str]]] = []
    group: list[tuple[str]] = []
    for col in reversed(cols):
        if all(c == " " for c in col) and group:
            groups.append(group)
            group = []
        else:
            group.append(col)
    groups.append(group)

    problems: list[list[str]] = []
    for g in groups:
        problem: list[str] = []
        for tup in g:
            digits = "".join(x for x in tup if x.isdigit())
            problem.append(digits)

        op = g[-1][-1]
        problem.append(op)
        problems.append(problem)

    for p in problems:
        *digits, op = p
        nums = list(map(int, digits))
        total += calculate(nums, op)

    return total
