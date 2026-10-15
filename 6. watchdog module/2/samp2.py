
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import glob
import os

class MyHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        
        if event.is_directory:
            print(f"\nCreated {event.src_path} directory") 
            all_filepaths = sorted(glob.glob(os.path.join(os.getcwd(), "SpectralData[1-5].dat")))
            print(all_filepaths)
        else:
            print(f"\nCreated {event.src_path} file") 
        

    def on_deleted(self, event):
        print(f"\nDeleted: {event.src_path}")

# Replace with the path I want to monitor
path = "."
handler = MyHandler()
observer = Observer()
observer.schedule(handler, path=path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    
    
observer.join()
