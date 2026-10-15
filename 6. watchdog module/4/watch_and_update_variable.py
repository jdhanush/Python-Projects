from watchdog.observers import Observer                  # This module cum class helps observe the events
from watchdog.events import FileSystemEventHandler       # This module cum class helps handle the observed events
from datetime import datetime
import pandas as pd
import numpy as np
import time 
import os


# Replace with the path I want to monitor, in this case, it is the current working directory
dir_under_observation = os.getcwd()


# This is the child class of "FileSystemEventHandler" class
class FileHandler(FileSystemEventHandler):
    
    def __init__(self):
        self.last_trigger_time = 0      # reference time variable for preventing from registering micro file-modification events
        self.i = 0                      # counter variable to indicate the number of times the file modifications happened
        
        
    # "on_created(self, event)" is an in-built function which handles the file/directory Creation events
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f"\n🔍 Detected file: '{filename}'")
            print(f"Detected filepath: \n'{event.src_path}'\n")
    
    
    # data_updater() is a purely user-defined function for creating fresh_data and accumulated data variables
    # it is expected that only the first line of the file is modified, so this function only looks at the first line for changes
    def data_updater(self, modfication_event_path):
        with open(modfication_event_path, 'r') as f:
            datalines = f.readlines()
            
        mat_dat = np.array([float(d) for d in datalines[0].split(',')])
        self.fresh_data = mat_dat
        
        if self.i == 0:
            # conversion of 'mat_dat' to array is an important step that's because,
            # mat_dat.shape = (N,) where as np.array([mat_dat]).shape = (1, N)            
            self.accumulated_data = np.array([mat_dat])     # this step ensure that the fed data is a row matrix.
        else:
            self.accumulated_data = np.vstack([self.accumulated_data, mat_dat])
        
        # 'accumulated_data_transposed' variable is deliberately defined outside else: block
        # Otherwise it won't work if the below variable is inside else: block    
        self.accumulated_data_transposed =  self.accumulated_data.T    
            
        self.i += 1     # the counter variable is updated once the modification is variables are detected
        
        
    # "on_modified(self, event)" is an in-built function which handles the file/directory Modification events        
    def on_modified(self, event):
        
        # if you only want to observe the file changes
        # Ignore directory events, which may also be triggered by metadata update events
        if event.is_directory: return

        current_time = time.time()

        # this prevents temporary files from triggering the on_modified event
        if "~" in event.src_path or event.src_path.endswith(".tmp"): return

        # Ignore duplicate micro modification events (0.3 seconds is usually enough for Windows filesystem noise)
        if current_time - self.last_trigger_time < 0.3:
            return
        
        # After waiting for 0.3 secs
        # the function now looks into the file and updates the variables acc. to the defined method
        self.data_updater(event.src_path)
        
        # updating the reference time variable with the current time    
        self.last_trigger_time = current_time
                 
        print(f"\n{datetime.now().strftime('%d-%B-%Y, %H:%M:%S')} - File is modified \nn={self.i} \nfresh_data: {self.fresh_data} \
              \naccumulated_data:\n{self.accumulated_data_transposed}\n ")
        

    

if __name__ == "__main__":
    
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



