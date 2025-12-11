def parse_input(data: str) -> tuple[list[list[int]], list[int]]:
    intervals: list[list[int]] = []
    ids: list[int] = []

    lines = data.splitlines()
    reading_intervals = True

    for line in lines:
        line = line.strip()

        if line == "":
            reading_intervals = False
            continue

        if reading_intervals:
            start, end = line.split("-")
            intervals.append([int(start), int(end)])
        else:
            ids.append(int(line))

    return intervals, ids


def part1(lines: tuple[list[list[int]], list[int]]) -> int:
    intervals, ids = lines
    fresh = 0

    for id in ids:
        for interval in intervals:
            start, end = interval
            if not (start <= id <= end):
                continue
            fresh += 1
            break

    return fresh


def merge_intervals(
    intervals: list[list[int]],
) -> list[list[int]]:
    merged: list[list[int]] = []
    intervals.sort()

    prev = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(interval[1], prev[1])
        else:
            merged.append(prev)
            prev = interval

    merged.append(prev)
    return merged


def part2(lines: tuple[list[list[int]], list[int]]) -> int:
    intervals, _ = lines
    fresh = 0
    intervals = merge_intervals(intervals)

    for interval in intervals:
        start, end = interval
        length = end - start + 1
        fresh += length

    return fresh
