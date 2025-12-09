import importlib
from pathlib import Path
import shutil

MAIN_DIR = Path(__file__).parent


def get_module(year: int, day: int):
    module_name = f"year{year}.day{day:02d}"
    return importlib.import_module(module_name)


def create_day(year: int, day: int):
    year_dir = MAIN_DIR / f"year{year}"
    day_template_path = MAIN_DIR / "template.py"
    day_stem = f"day{day:02d}"

    day_path = year_dir / f"{day_stem}.py"
    input_path = get_input_path(year, day, example=False)
    example_input_path = get_input_path(year, day, example=True)

    created = 0
    if not day_path.exists():
        day_path.parent.mkdir(parents=True, exist_ok=True)
        _ = shutil.copy(day_template_path, day_path)
        created += 1
        print(f"Created {day_path}")

    if not input_path.exists():
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.touch()
        created += 1
        print(f"Created {input_path}")

    if not example_input_path.exists():
        example_input_path.parent.mkdir(parents=True, exist_ok=True)
        example_input_path.touch()
        created += 1
        print(f"Created {example_input_path}")

    if created == 0:
        print("All files already exist.")


def get_input_path(year: int, day: int, example: bool = False) -> Path:
    year_dir = MAIN_DIR / f"year{year}"
    file_stem = f"day{day:02d}"
    input_folder_name = "example_inputs" if example else "inputs"
    return year_dir / input_folder_name / f"{file_stem}.txt"
