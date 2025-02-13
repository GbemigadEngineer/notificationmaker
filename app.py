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