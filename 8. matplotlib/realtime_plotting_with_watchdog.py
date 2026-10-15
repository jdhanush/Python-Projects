import pandas as pd
import matplotlib.pyplot as plt

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
import os

# --------------------------------------------------
# GLOBAL FLAG
# --------------------------------------------------

csv_updated = False

# --------------------------------------------------
# PLOT SETUP
# --------------------------------------------------

figure, axis = plt.subplots()

line1, = axis.plot([], [], label='Channel 1')
line2, = axis.plot([], [], label='Channel 2')

axis.legend(loc='upper left')
axis.grid(True)

# --------------------------------------------------
# UPDATE FUNCTION
# --------------------------------------------------

def update_plot():

    try:

        data = pd.read_csv('data.csv')

        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']

        line1.set_data(x, y1)
        line2.set_data(x, y2)

        axis.relim()
        axis.autoscale_view()

        figure.canvas.draw_idle()

    except Exception as error:
        print(error)

# --------------------------------------------------
# WATCHDOG EVENT HANDLER
# --------------------------------------------------

class FileChangeHandler(FileSystemEventHandler):

    def on_modified(self, event):

        global csv_updated

        if event.src_path.endswith('data.csv'):

            print("CSV Updated")

            csv_updated = True

# --------------------------------------------------
# WATCHDOG OBSERVER
# --------------------------------------------------

path = os.getcwd()

event_handler = FileChangeHandler()

observer = Observer()

observer.schedule(event_handler, path=path, recursive=False)

observer.start()

# --------------------------------------------------
# NON-BLOCKING PLOT
# --------------------------------------------------

plt.show(block=False)

# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------

try:

    while True:

        if csv_updated:

            csv_updated = False

            update_plot()

        plt.pause(0.1)

except KeyboardInterrupt:

    observer.stop()

    print("\n🛑 Watchdog stopped Observing")

observer.join()