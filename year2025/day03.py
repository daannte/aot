def parse_input(data: str) -> list[str]:
    return data.splitlines()


def right_side_maxima(digits: list[int]) -> list[int]:
    n = len(digits)
    res = [0] * n
    max_so_far = -1

    for i in range(n - 1, -1, -1):
        res[i] = max_so_far
        max_so_far = max(max_so_far, digits[i])

    return res


def max_jolt_for_line(digits: list[int]) -> int:
    right_max = right_side_maxima(digits)
    best = -1
    for i, d in enumerate(digits[:-1]):
        if right_max[i] == -1:
            continue

        jolt = d * 10 + right_max[i]
        best = max(best, jolt)

    return best


def part1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        digits = list(map(int, line.strip()))
        total += max_jolt_for_line(digits)
    return total


def part2(lines: list[str]) -> int:
    return 0
