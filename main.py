"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
import subprocess

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

py_env_path = "destination.py"

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("Do not return any formatting such as markdown, quotes, or backticks. Provide only the raw Python script USERS PROMPT: Hey gemini can you generate a python script that will write a tex file for a mock resume with clean format and then convert the tex file into docx using pandoc?")

response = str(response.text)

with open(py_env_path, 'w') as file:
    file.write(response)


command = ['python', py_env_path]    

subprocess.run(command, check=True)

print(response)

