import os
from config import MAX_CHARACTERS
from google.genai import types

def get_file_content(working_directory, file_path):

    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))

    # boundary check first
    if not (target_abs == wd_abs or target_abs.startswith(wd_abs + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # must be a file
    if not os.path.isfile(target_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_abs, "r") as f:
            file_content_string = f.read(MAX_CHARACTERS)
            extras = f.read(1)
            if extras:
                return f'{file_content_string}\n[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read contents of a file up to a max character limit, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to read.",
            ),
        },
        required=["file_path"],
    ),
)