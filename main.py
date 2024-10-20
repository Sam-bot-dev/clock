from tkinter import * # It is a basic grapic user interface (GUI) library in python
import datetime # It is a module for manupilating date and time
import time # This returns current time
import winsound # This provides to windows basic sound playing capabilities

# Create Object
root = Tk()

ef alarm():
    # Infinite Loop
    while True:
        # Set Alarm 
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
