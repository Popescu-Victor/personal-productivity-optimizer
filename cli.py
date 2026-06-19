from dotenv import load_dotenv
import os
import sys
import argparse

raw_input = sys.argv[1:]
if len(raw_input) == 0:
    print("No arguments provided. Please provide a command.")
    sys.exit(1)
else:
    command = raw_input[0].strip()
    print(f"Command received: {command}")