
def add_skateboarding_reminder(file_path):
  """Opens a text file and adds a reminder to go skateboarding.

  Args:
    file_path: The path to the text file.
  """

  try:
    with open(file_path, "a") as file:
      file.write("\nDon't forget to go skateboarding!\n")
    print("Reminder added successfully!")
  except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'")

# Get the file path from the user
file_path = input("Enter the path to your text file: ")

# Add the skateboarding reminder to the file
add_skateboarding_reminder(file_path)

