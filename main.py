import argparse

from utils import create_day, get_module, get_input_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Advent of Code solution")
    parser.add_argument("year", type=int, help="Year of the puzzle")
    parser.add_argument("day", type=int, help="Day of the puzzle")
    parser.add_argument(
        "-e", "--example", action="store_true", help="Use example input"
    )
    parser.add_argument("-a", "--add", action="store_true", help="Create new day files")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.add:
        create_day(args.year, args.day)
    else:
        input_file_path = get_input_path(args.year, args.day, args.example)
        data = input_file_path.read_text()
        module = get_module(args.year, args.day)

        lines = module.parse_input(data)

        print(module.part1(lines))
        print(module.part2(lines))


if __name__ == "__main__":
    main()
