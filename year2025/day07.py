from collections import deque
from pprint import pprint


def parse_input(data: str):
    grid = [list(line) for line in data.splitlines()]
    grid[1][len(grid[0]) // 2] = "|"
    return grid


def part1(grid: list[list[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    splits = 0
    row = 1

    while row < rows - 1:
        for col in range(cols):
            if grid[row][col] == "|":
                if grid[row + 1][col] == "^":
                    splits += 1
                    grid[row + 1][col + 1] = "|"
                    grid[row + 1][col - 1] = "|"
                else:
                    grid[row + 1][col] = "|"
        row += 1

    return splits


def part2(lines: list[str]) -> int:
    return 0
