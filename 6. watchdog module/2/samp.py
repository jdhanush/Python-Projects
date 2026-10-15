import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File {event.src_path} has been modified')
    
    def on_any_event(self, event):
        print('\nAn new event is registered')

    def on_created(self, event):
        print(f'File {event.src_path} has been created')

    def on_deleted(self, event):
        print(f'File {event.src_path} has been deleted')
        
    def on_moved(self, event):
        print(f'File {event.src_path} is moved')    
        
        
        
if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()        # Signals the thread to start

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()     # Signals the thread to stop
    
    observer.join()        # Wait here until the thread actually terminates