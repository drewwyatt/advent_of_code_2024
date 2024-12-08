import importlib
import sys

def run_solution(day):
    try:
        # Dynamically import the solution module for the given day
        module_name = f"solutions.day_{day:02d}.solution"
        solution_module = importlib.import_module(module_name)
        
        # Check if the solution module has a `solve` function
        if hasattr(solution_module, "solve"):
            from common.utils import read_input
            input_data = read_input(f"solutions/day_{day:02d}/input.txt")
            result = solution_module.solve(input_data)
            print(f"Day {day} Solution: {result}")
        else:
            print(f"No `solve` function found in {module_name}")
    except ModuleNotFoundError:
        print(f"Solution for day {day:02d} not found.")
    except Exception as e:
        print(f"Error running solution for day {day:02d}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <day>")
    else:
        try:
            day = int(sys.argv[1])
            run_solution(day)
        except ValueError:
            print("Invalid day. Please provide a numeric day.")
