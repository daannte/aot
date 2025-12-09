def parse_input(data: str):
    return data.splitlines()


def rotate(pointer: int, direction: str, clicks: int) -> int:
    return (pointer + clicks) % 100 if direction == "R" else (pointer - clicks) % 100


def part1(lines: list[str]) -> int:
    pointer = 50
    zeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])
        pointer = rotate(pointer, direction, clicks)
        zeroes += 1 if pointer == 0 else 0

    return zeroes


def passes(pointer: int, direction: str, clicks: int) -> int:
    count = 0

    for _ in range(clicks):
        pointer = (pointer + 1) % 100 if direction == "R" else (pointer - 1) % 100
        count += 1 if pointer == 0 else 0

    return count


def part2(lines: list[str]) -> int:
    pointer = 50
    zeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])
        zeroes += passes(pointer, direction, clicks)
        pointer = rotate(pointer, direction, clicks)

    return zeroes
