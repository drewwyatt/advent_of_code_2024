import os
import inspect

def read_input(file_path="input.txt"):
    """
    Reads the content of the given input file.
    If the file_path is relative, it resolves it relative to the calling script's directory.
    """
    # Get the directory of the calling script
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    # Resolve the full path
    full_path = os.path.join(caller_dir, file_path) if not os.path.isabs(file_path) else file_path

    with open(full_path, "r") as f:
        return f.read().strip()
