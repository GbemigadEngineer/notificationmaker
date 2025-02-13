# First we inport all the necessary libraries and modules
import time
import datetime
import json
from plyer import notification
from playsound import playsound
import threading 
import os


# Alarm sound file 

Alarm_Sound = "mixkit-vintage-warning-alarm-990.wav"

# Interval for weekend reminders (in seconds)

Reminder_Interval = 4 * 60 * 60 # Every 4 hours

# File to store the tasks in
Task_File = "weekend_tasks.json"

# Function to play alarm sound
def play_alarm():
    playsound(Alarm_Sound)

# Function to show notification
def show_notification(title, message):
# display a pop-up notification.
    notification.notify(
        title = title, #Title of the notification
        message = message, #Message of the notification
        app_name = " My Weekend Reminder", #Name of the app
        timeout = 30 #notication will dissapear after 30 seconds

    )

        # Start a new thread to play the alarm sound
    threading.Thread(target=play_alarm).start()



"""The load_tasks function attempts to load tasks from a JSON file specified by Task_File. 
If the file exists, it reads and parses the JSON data into a Python dictionary and returns it. 
If the file does not exist, it returns an empty dictionary. 
This ensures that the function always returns a dictionary, whether or not the file is present."""
def load_tasks():
    # Load the tasks from the file
    if os.path.exists(Task_File):
        with open(Task_File, "r") as file:
            return json.load(file)
    return{}




"""

Load Existing Tasks: It first loads the existing tasks from a file using the load_tasks function.
Update Tasks: It checks if the given date already exists in the tasks dictionary:
If the date exists, it extends the list of tasks for that date with the new tasks.
If the date does not exist, it creates a new list of tasks for that date.
Save Updated Tasks: It opens the task file in write mode and saves the updated tasks dictionary to the file in JSON format.
Notification: It shows a notification to the user indicating whether the tasks were successfully saved or if an error occurred.
The function handles exceptions and provides user feedback through notifications.

"""

def save_tasks(date, new_tasks):
    try:
        # Load the existing tasks from the file
        tasks = load_tasks()

        # Check if the date already exists in the tasks dictionary
        if date in tasks:
            # If the date exists, extend the list of tasks for that date with the new tasks
            tasks[date].extend(new_tasks)
        else:
            # If the date does not exist, create a new list of tasks for that date
            tasks[date] = new_tasks

        # Open the task file in write mode to save the updated tasks
        with open(Task_File, "w") as file:
            # Serialize the tasks dictionary to JSON and write it to the file with indentation for readability
            json.dump(tasks, file, indent=4)
        
        # Show a notification to the user indicating that the tasks have been saved
        show_notification("✅ Weekend Tasks Saved!", "Your tasks have been recorded!")
    except Exception as e:
        # Show a notification to the user indicating that the tasks could not be saved
        show_notification("❌ Couldn't Add Tasks", f"An error occurred: {str(e)}")



def get_tasks(date):
    """Retrieves saved weekend tasks from file."""
    tasks = load_tasks()
    return tasks.get(date, ["No tasks found. Please set your tasks on Wednesday or Friday!"])



def wednesday_friday_prompts():
    # Runs a prompt every wednesday and friday for the user to add tasks.
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    print("\n Enter Tasks for the weekend (type 'done' when finished): ")

    tasks = []

    while True:
        task = input('Task:')
        if task.lower() == 'done':
            break
        tasks.append(task)

    save_tasks(today_date, tasks)