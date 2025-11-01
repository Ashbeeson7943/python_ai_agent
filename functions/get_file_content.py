import os
from config import MAX_CHARACTERS

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

