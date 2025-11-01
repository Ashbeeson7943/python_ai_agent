import os

def write_file(working_directory, file_path, content):
    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))

    # boundary check first
    if not (target_abs.startswith(wd_abs + os.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
   
    os.makedirs(os.path.dirname(target_abs), exist_ok=True)
    
    try:
        with open(target_abs , "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"