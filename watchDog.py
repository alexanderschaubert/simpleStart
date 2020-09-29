import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            file = folder_track + "\\" +filename
            new_path = folder_dest + "\\" +filename
            os.rename(file, new_path)

folder_track = "C:\\Users\\alexander.schaubert\\Downloads"
folder_dest = "C:\\Users\\alexander.schaubert\\Desktop\\test"

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()


try:
 while(True):
     time.sleep(3)
except KeyboardInterrupt:
    observer.stop()

observer.join()