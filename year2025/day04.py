from collections.abc import Generator


def parse_input(data: str) -> list[str]:
    return data.splitlines()


def neighbours(i: int, j: int) -> Generator[tuple[int, int], None, None]:
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            yield i + di, j + dj


def can_access(i: int, j: int, lines: list[list[str]]) -> bool:
    count = 0

    for ni, nj in neighbours(i, j):
        if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]):
            if lines[ni][nj] != "@":
                continue
            count += 1

    return count < 4


def part1(lines: list[str]) -> int:
    """
    Find rolls to remove that have < 4 adjacent rolls
    """
    grid = [list(row) for row in lines]

    total = 0
    for i, line in enumerate(grid):
        for j, roll in enumerate(line):
            if roll != "@" or not can_access(i, j, grid):
                continue
            total += 1

    return total


def part2(lines: list[str]) -> int:
    """
    Basically repeat part 1 until we cant remove anymore
    """
    grid: list[list[str]] = [list(row) for row in lines]
    total = 0

    while True:
        to_remove: list[tuple[int, int]] = []

        for i, line in enumerate(grid):
            for j, roll in enumerate(line):
                if roll != "@" or not can_access(i, j, grid):
                    continue
                to_remove.append((i, j))

        if not to_remove:
            break

        for i, j in to_remove:
            grid[i][j] = "."
            total += 1

    return total
