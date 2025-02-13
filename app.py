# First we inport all the necessary libraries and modules
import time
import datetime
import json
from plyer import notification
from playsound import playsound
import threading 
import os


# Alarm sound file 

Alarm_Sound = "mixkit-alarm-digital-clock-beep-989.wav"

# Interval for weekend reminders (in seconds)

Reminder_Interval = 4 * 60 * 60 # Every 4 hours



