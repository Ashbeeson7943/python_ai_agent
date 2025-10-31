import os

def get_files_info(working_directory, directory=""):
    print("\n------------------")
    print(f"Inputs: wd={working_directory}, dir={directory}")

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

    if not abs_path.__contains__(working_directory):
        response_intro.append(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "".join(response_intro)
    

    response_body = []

    # Get files/directories
    listed_files = os.listdir(path)
    
    for file in listed_files:
        f_size = "1"
        is_dir = False
        response_body.append(f"    {file}: file_size={f_size} bytes, is_dir={is_dir}")

    print("------------------")
    return "".join(response_intro) + "\n".join(response_body)
