import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    verbose = False
    if len(sys.argv) < 2:
        print(f"Enter a prompt!\nUsage: uv run main.py <PROMPT>")
        sys.exit(1)
    
    if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
        verbose = True

    user_prompt = sys.argv[1]

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")

    message_history = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=message_history)
    print(response.text)
    


if __name__ == "__main__":
    main()
