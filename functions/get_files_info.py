import os
from google.genai import types

def get_files_info(working_directory, directory="."):    

    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, directory))

    header = "Result for current directory:" if directory == "." else f"Result for '{directory}' directory:"

    # boundary check first
    if not (target_abs == wd_abs or target_abs.startswith(wd_abs + os.sep)):
        return f"{header}\n    Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

    # must be a directory
    if not os.path.isdir(target_abs):
        return f"{header}\n    Error: \"{directory}\" is not a directory"

    try:
        entries = os.listdir(target_abs)
    except Exception as e:
        return f"{header}\n    Error: {e}"

    lines = []
    for name in entries:
        p = os.path.join(target_abs, name)
        try:
            size = os.path.getsize(p)
            is_dir = os.path.isdir(p)
        except Exception as e:
            return f"{header}\n    Error: {e}"
        lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

    return header + ("\n" + "\n".join(lines) if lines else "")

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)