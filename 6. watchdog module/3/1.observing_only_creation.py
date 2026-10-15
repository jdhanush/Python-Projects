from watchdog.observers import Observer                  # This module cum class helps observe the events
from watchdog.events import FileSystemEventHandler       # This module cum class helps handle the observed events
import pandas as pd
import time 
import os


# Replace with the path I want to monitor
dir_under_observation = os.getcwd()
WATCH_FOLDER = "watchdog-folder"


# This is the child class of "FileSystemEventHandler" class
class FileHandler(FileSystemEventHandler):
    
    # "on_created(self, event)" is an in-built function which handles the file/directory Creation event
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f"\n🔍 Detected file: '{filename}'")
            print(f"Path of file responsible for creation event: \n{event.src_path} \ntype of path: {type(event.src_path)}\n")
        






# Standard way of Initializing the Observer and EventHandling classes
#########################################################################

# Creating the object of EventHandling class "FileHandler"
handler = FileHandler()             

# Creating the object of Observer class that we imported
observer = Observer()               

# Running the schedule() function in the 'observer' object
# We are passing EventHandling child class, the directory under observation, and whether to look into sub-directories(True) or not(False)
observer.schedule(handler, path=dir_under_observation, recursive=False)




# The start() in the Observer class will start the observation
observer.start()
print(f"\n👀 Watchdog started observing the required directory. In this case: \n{os.getcwd()} \n")

# This is an Exception Handling loop which runs(starts observation) perpetually (non-stop) but ...
# stops(stops observation) on KeyboardInterrupt (Ctrl + C)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("\n🛑 Watchdog stopped Observing")
    
# This is for continuing the thread    
observer.join()



# "event.src_path" gives us the full path of the file/directory which was responsible for the event in "event.src_path"


