# GENERATE CODE BLOCKS

import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate(task):
    prompt = f"""
        You are an agent tasked with generating Python code to assist with a specific task. Respond with valid, exectuable Python code. Make sure to obey Python's indentation syntax. Use only built-in modules.
        The task: ${task}
    """
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return completion["choices"][0]["message"]["content"]