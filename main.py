import importlib
import sys
from typing import Optional


def run_solution(day: int, part: Optional[int] = None):
    try:
        # Dynamically import the solution module for the given day
        module_name = f"solutions.day_{day:02d}.solution"
        solution_module = importlib.import_module(module_name)

        # Check if the solution module has a `solve` function
        if hasattr(solution_module, "solve"):
            from common.utils import read_input

            input_data = read_input(f"solutions/day_{day:02d}/input.txt")

            if part:
                result = solution_module.solve(input_data, part=part)
                print(f"Day {day} Part {part} Solution: {result}")
            else:
                result1 = solution_module.solve(input_data, part=1)
                result2 = solution_module.solve(input_data, part=2)
                print(f"Day {day} Part 1 Solution: {result1}")
                print(f"Day {day} Part 2 Solution: {result2}")
        else:
            print(f"No `solve` function found in {module_name}")
    except ModuleNotFoundError:
        print(f"Solution for day {day:02d} not found.")
    except Exception as e:
        print(f"Error running solution for day {day:02d}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <day> [<part>]")
    else:
        try:
            day = int(sys.argv[1])
            part = int(sys.argv[2]) if len(sys.argv) > 2 else None
            run_solution(day, part)
        except ValueError:
            print("Invalid arguments. Please provide numeric day and part values.")
