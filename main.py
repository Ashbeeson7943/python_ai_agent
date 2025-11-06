import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT)

def main():
    verbose = False
    if len(sys.argv) < 2:
        print(f"Enter a prompt!\nUsage: uv run main.py <PROMPT>")
        sys.exit(1)
    
    if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
        verbose = True

    user_prompt = sys.argv[1]

    
    message_history = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=message_history, config=config)
    res_func_calls = response.function_calls
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")


    if not res_func_calls == None: 
        for function_call_part in res_func_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    


if __name__ == "__main__":
    main()
