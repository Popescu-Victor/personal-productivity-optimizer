import dotenv
import os
import sys
import argparse
from google import genai

# REQL - PowerShell tool for automating work and personal tasks.

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
        if command == "ask": # "ask" calls on Gemini Flash api
            context = " Give a short and simple answer"
            call_gemini_api(str(raw_input[1:]) + context)
        if command == "scrape":
            pass
        if command == "cron":
            pass
        if command == "search":
            pass
        if command == "correlation":
            pass
        if command == "search":
            pass
        if command == "thm":
            pass
        if command == "git":
            pass
        if command == "ilias":
            pass
        if command == "anon":
            from tkinter import filedialog
            folder_path = filedialog.askdirectory(title="Select a folder")
            for file in folder_path:
                pass # randomize names



main()