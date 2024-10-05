# RubyOnPC: Dynamic Script Generator & Executor

RubyOnPC is an innovative desktop application that leverages the AI to generate and execute Python scripts based on user-defined prompts. It harnesses Google’s Gemini generative AI model to automate tasks.

## Features

- **AI-Powered Script Generation**: Generate Python scripts dynamically from natural language prompts using Gemini's generative capabilities.
- **User-Friendly GUI**: Intuitive graphical interface built with Tkinter, allowing easy interaction and task execution.
- **Error Handling**: Robust error handling for script execution, providing feedback and debugging suggestions.
- **Environment Variable Management**: Securely manage your API keys and other environment variables with `.env` support.

## Getting Started

### Prerequisites

Before you start, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- A Google account with access to the Gemini API

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/RubyOnPC.git
   cd RubyOnPC
   ```

2. **Install required packages**:
   Use pip to install the necessary libraries:
   ```bash
   pip install google-generativeai python-dotenv tkinter
   ```

3. **Set up your environment variables**:
   Create a `.env` file in the project root directory and add your API key:
   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the application**:
   Execute the main script to launch the GUI:
   ```bash
   python main.py
   ```

### Usage

1. **Input Prompt**: Enter a task prompt in the provided text area.
2. **Execute Task**: Click the "Execute Task" button to generate and run the Python script based on your input.
3. **View Output**: If the task is executed successfully, you’ll see a confirmation message. If there's an error, the application will provide a debug prompt with details.

### Code Overview

The main components of the code include:

- **Environment Setup**: Uses `dotenv` to load environment variables.
- **AI Model Configuration**: Configures the Gemini AI model for script generation.
- **GUI Implementation**: Built with Tkinter for a seamless user experience.
- **Error Handling**: Catches and reports errors during script execution, prompting for potential fixes.

### Example Prompt

You can try prompts like:

- "Create a script that calculates the Fibonacci series."
- "Write a function to scrape data from a website."

### Contribution

Contributions are welcome! If you'd like to enhance RubyOnPC, please fork the repository and submit a pull request. Be sure to follow the code style and include tests for any new features.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
