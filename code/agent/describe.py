# DESCRIBE CODE BLOCKS

import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def describe(code):
    prompt = f"""
        You are an agent tasked with describing Python code to help a user understand what it does. Respond with a clear, concise explanation of what the code does. Be sure to make note of any built-in or external Python libraries used in the code.
        The code: {code}
    """
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return completion["choices"][0]["message"]["content"]