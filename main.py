import os
import google.generativeai as genai
from dotenv import load_dotenv
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import json
import time
import threading  # Import threading to run tasks in a separate thread

# Load environment variables
load_dotenv()

# Set up the API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# File path for the target script
py_env_path = "target.py"

# System prompt for the model
systemPrompt = '''Generate a JSON object with three string variables: 
- The first string variable should be called 'command' and contain a shell command for installations like "pip install" and only installations. 
- The second string variable should be called 'script' and contain a Python script with proper indentation and formatting. Ensure it's formatted as raw plain text with no extra symbols, markdown, or backticks. 
- The third string variable should be called 'response' and contain the expected output from running the script. 
Ensure the JSON object is in plain text with no special formatting or extra characters. User's prompt '''

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
    tools='code_execution'
)

def do_task(prompt):
    """Generate a script from the prompt and save it to a file."""
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(systemPrompt + prompt)
    return response.text

def run_script_in_thread():
    """Run the execute_script function in a separate thread."""
    loading_label.pack(pady=10)  # Show the loading label
    execute_button.configure(state="disabled")  # Disable the button during execution
    thread = threading.Thread(target=execute_script)
    thread.start()
    root.after(100, check_thread, thread)  # Check the thread periodically

def check_thread(thread):
    """Check if the thread has finished running."""
    if thread.is_alive():
        root.after(100, check_thread, thread)
    else:
        loading_label.pack_forget()  # Hide the loading label once done
        execute_button.configure(state="normal")  # Re-enable the button

def execute_script():
    """Execute the generated Python script and show a success message."""
    prompt = prompt_text.get("1.0", ctk.END).strip()
    if prompt:
        response = do_task(prompt=prompt)
        response = str(response)

        response = response.strip('```')
        response = response.strip('json')
        print(response)
        
        json_response = json.loads(response)
        
        command = json_response['command']
        script = json_response['script']
        comment = json_response['response']
        
        subprocess.run(command)

        with open(py_env_path, 'w') as file:
            file.write(script)
        success = False
        while not success:
          try:
              # Attempt to execute the script
              subprocess.run(['python', py_env_path], check=True)
              messagebox.showinfo("Success", "Task Executed Successfully!", comment)
              success = True  # If the script runs successfully, exit the loop
          except subprocess.CalledProcessError as e:
              # If an error occurs, handle the failure
              error_message = f"Failed to execute the script.\nExit Code: {e.returncode}\nOutput: {e.output.decode() if e.output else 'No output'}"
              redo_string = f"this is the error {error_message} and this is the json {json_response} debug it and return in the same format"
              
              # Retry mechanism (or any logging you want here)
              print("Error occurred:", redo_string)
              messagebox.showerror("Execution Error", "Redoing task. Waiting for retry...")
              
              # Optionally, add a delay before retrying
              time.sleep(4)  # Add a small delay before retrying to avoid spamming                       
        
        prompt_text.delete("1.0", ctk.END)  # Clear input field
    else:
        messagebox.showwarning("Input Error", "Please enter a prompt.")

def create_gui():
    """Set up the main GUI components."""
    ctk.set_appearance_mode("dark")  # Set the theme to dark mode
    ctk.set_default_color_theme("blue")  # Set the color theme

    global root
    root = ctk.CTk()
    root.title("RubyOnPC")
    root.geometry("500x400")

    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="Enter your task prompt:", font=("Arial", 16))
    label.pack(pady=10)

    global prompt_text
    prompt_text = ctk.CTkTextbox(frame, height=150, width=400)
    prompt_text.pack(pady=10)

    global execute_button
    execute_button = ctk.CTkButton(frame, text="Execute Task", command=run_script_in_thread, fg_color="green", hover_color="darkgreen")
    execute_button.pack(pady=10)

    global loading_label
    loading_label = ctk.CTkLabel(frame, text="Loading...", font=("Arial", 16))  # This label will show the loading message

    exit_button = ctk.CTkButton(frame, text="Exit", command=root.quit, fg_color="red", hover_color="darkred")
    exit_button.pack(pady=5)

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
