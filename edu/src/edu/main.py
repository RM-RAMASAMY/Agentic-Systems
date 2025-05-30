#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv
import os

# Add this line to set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from .env
load_dotenv()

# Must precede any llm module imports
from langtrace_python_sdk import langtrace

# Get the API key from the environment
# langtrace_api_key = os.getenv("LANGTRACE_API_KEY")
# if not langtrace_api_key:
#     raise ValueError("LANGTRACE_API_KEY is not set in the .env file")

# langtrace.init(api_key=langtrace_api_key)

from datetime import datetime

from edu.crew import Edu

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
MY_TOPIC = "Containerization vs Virtualization"
def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': MY_TOPIC,
        'current_year': str(datetime.now().year)
    }
    
    try:
        Edu().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": MY_TOPIC
    }
    try:
        Edu().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Edu().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": MY_TOPIC,
        "current_year": str(datetime.now().year)
    }
    try:
        Edu().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
