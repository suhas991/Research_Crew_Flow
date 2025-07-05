#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from job_flow.crew import JobFlow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("Enter the topic to research about:")
    research_topic = input()

    inputs = {
        'topic': research_topic ,
        'current_year': str(datetime.now().year)
    }
    
    try:
        JobFlow().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
