import os
import google.generativeai as genai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
import subprocess

# Load environment variables
load_dotenv()

# Set up the API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# File path for the target script
py_env_path = "target.py"

# System prompt for the model
systemPrompt = "Do not return any formatting such as markdown, quotes, or backticks. Provide only the raw Python script as plain text."

# Model generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def do_task(prompt):
    """Generate a script from the prompt and save it to a file."""
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(systemPrompt + prompt)
    response = response.text.strip('```')  
    response = response.strip('python')
    
    with open(py_env_path, 'w') as file:
        file.write(response)
        print(response)

def execute_script():
    """Execute the generated Python script and show a success message."""
    prompt = prompt_text.get("1.0", tk.END).strip()
    if prompt:
        do_task(prompt=prompt)
        
        try:
            subprocess.run(['python', py_env_path], check=True)
            messagebox.showinfo("Success", "Task Executed Successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Execution Error", "Redo.")
            error_message = f"Failed to execute the script.\nExit Code: {e.returncode}\nOutput: {e.output.decode() if e.output else 'No output'}"
            with open(py_env_path, 'r') as file:
                code = file.read()
            redo_string = f"this is the error {error_message} and this is the code {code} debug"    
            redo_string = systemPrompt + redo_string
            do_task(prompt=redo_string)
            subprocess.run(['python', py_env_path], check=True)                        
            
        
        prompt_text.delete("1.0", tk.END)  # Clear input field
    else:
        messagebox.showwarning("Input Error", "Please enter a prompt.")

def create_gui():
    """Set up the main GUI components."""
    root = tk.Tk()
    root.title("RubyOnPC")
    
    # Set window size
    root.geometry("400x300")
    
    # Label for the prompt
    label = tk.Label(root, text="Enter your task prompt:", font=("Arial", 12))
    label.pack(pady=10)
    
    # Text area for prompt input
    global prompt_text
    prompt_text = tk.Text(root, height=5, width=40)
    prompt_text.pack(pady=10)

    # Execute button
    save_button = tk.Button(root, text="Execute Task", command=execute_script, bg="green", fg="white")
    save_button.pack(pady=10)
    
    # Exit button
    exit_button = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white")
    exit_button.pack(pady=5)
    
    root.mainloop()

# Run the GUI
create_gui()
