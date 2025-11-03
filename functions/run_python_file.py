import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    
    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))

    # boundary check first
    if not (target_abs == wd_abs or target_abs.startswith(wd_abs + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_abs):
        return f'Error: File "{file_path}" not found.'

    if not target_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    command_array = [sys.executable, file_path]
    command_array.extend(args)
    try:
        
        completed_process = subprocess.run(args=command_array, capture_output=True, timeout=30, cwd=wd_abs, text=True)
        msg = f"STDOUT: {completed_process.stdout}\nSTDERR {completed_process.stderr}"
        if not completed_process.stdout:
            msg += f"No output produced."
        if not completed_process.returncode == 0:
            msg += f"\nProcess exited with code {completed_process.returncode}"
        return msg
    except Exception as e:
        return f"Error: executing Python file: {e}"