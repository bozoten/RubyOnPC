import datetime

def add_reminder(filename, reminder_text):
    """Adds a reminder to a text file."""
    with open(filename, "a") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n\nReminder: {reminder_text} - Added on {current_time}")

filename = input("Enter the name of the text file: ")
reminder_text = "Don't forget to go skateboarding!"

add_reminder(filename, reminder_text)
print(f"Reminder added to '{filename}'")
