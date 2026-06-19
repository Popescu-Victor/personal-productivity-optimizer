import dotenv
import os
import sys
import argparse
from google import genai


def call_gemini_api(prompt):
    api_key = dotenv.get_key(dotenv.find_dotenv(), "GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    print(response.text)


def main():
    raw_input = sys.argv[1:]
    if len(raw_input) == 0:
        print("No arguments provided. Please provide a command.")
        sys.exit(1)
    else:
        command = raw_input[0].strip()
        if command == "ask":
            call_gemini_api(raw_input[1])
