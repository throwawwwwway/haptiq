import threading
import time
import tkinter as tk

from pattern import Oscilate
from raw import Raw
from raw import Point


def init_raw():
    return Raw(['actA', 'actB', 'actC', 'actD'])


def motion(event, raw):
    x, y = event.x, event.y
    raw.set_position(Point(x, y))


def haptiq_simulator(raw):
    root = tk.Tk()  # Launch panel
    root.bind('<Motion>', lambda event, raw=raw: motion(event, raw))
    root.mainloop()


def network_behavior(raw):
    pattern = Oscilate()
    while 1:
        point = raw.get_position()
        print("level should be now: " + str(pattern.next_level()))
        time.sleep(3)

raw = init_raw()

simu = threading.Thread(target=network_behavior, args=(raw,))
simu.start()

haptiq_simulator(raw)
