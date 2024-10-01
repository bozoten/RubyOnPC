"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
import subprocess
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

py_env_path = "target.py"

systemPrompt = "Do not return any formatting such as markdown, quotes, or backticks. Provide only the raw Python script as plain text."

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

def do_task(prompt):
  chat_session = model.start_chat(
    history=[
    ]
  )

  response = chat_session.send_message(systemPrompt + prompt)
  response = response.text.strip('```')  
  with open(py_env_path, 'w') as file:
      file.write(response)
      print(response)

def gui():
  prompt = prompt_text.get("1.0", tk.END).strip()

  if prompt:
     do_task(prompt=prompt)
     command = ['python', py_env_path]    

     subprocess.run(command, check=True)
     messagebox.showinfo("Success", "Task Executed!")
     prompt_text.delete("1.0", tk.END)  
  else:
     messagebox.showwarning("Input Error", "Please enter a prompt.")  
  
root = tk.Tk()
root.title("RubyOnPC")

prompt_text = tk.Text(root, height=5, width=30)
prompt_text.pack(pady=10)

save_button = tk.Button(root, text="Execute", command=gui)
save_button.pack(pady=5)

root.mainloop()




