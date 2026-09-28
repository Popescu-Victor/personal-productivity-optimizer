import dotenv
import os
import sys
import argparse
from google import genai


def call_gemini_api(prompt):
    api_key = dotenv.get_key(dotenv.find_dotenv(), "GEMINI_API_KEY") # REMINDER: Set Gemini Key in an .env file before running!

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    print(response.text)

