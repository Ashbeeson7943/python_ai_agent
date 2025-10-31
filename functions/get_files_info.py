import os

def get_files_info(working_directory, directory=""):

    # Set up response
    response_intro = []
    if directory == ".":
        response_intro.append(f"Result for current directory:\n")
    else:
        response_intro.append(f"Result for '{directory}' directory:\n")

    # Create path
    path = os.path.join(working_directory, directory)
    # perform validation checks 
    if not os.path.isdir(path):
        response_intro.append(f'    Error: "{directory}" is not a directory')
        return "".join(response_intro)
    
    abs_path = os.path.abspath(path)

    if not abs_path.startswith(os.path.abspath(working_directory) + os.sep):
        response_intro.append(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "".join(response_intro)
    

    response_body = []

    # Get files/directories
    listed_files = os.listdir(path)
    
    for file in listed_files:
        file_path = path + os.sep + file
        f_size = ""
        is_dir = False
        try:
            f_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
        except Exception as e:
            return f"Error: {e}"
        response_body.append(f"- {file}: file_size={f_size} bytes, is_dir={is_dir}")

    return "".join(response_intro) + "\n".join(response_body)
