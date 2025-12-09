def parse_input(data: str):
    return data.strip().split(",")


def part1(lines: list[str]) -> int:
    total = 0
    for r in lines:
        first, last = map(int, r.split("-"))
        for id in range(first, last + 1):
            s = str(id)
            n = len(s)
            if n % 2 != 0:
                continue

            mid = n // 2
            if s[mid:] == s[:mid]:
                total += id

    return total


# ------ Part 2 ----- #


def is_invalid(id: str) -> bool:
    n = len(id)

    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue

        pattern = id[:size]
        repeats = n // size

        if pattern * repeats == id and repeats >= 2:
            return True

    return False


def part2(lines: list[str]) -> int:
    total = 0
    for r in lines:
        first, last = map(int, r.split("-"))

        for id in range(first, last + 1):
            if is_invalid(str(id)):
                total += id

    return total
