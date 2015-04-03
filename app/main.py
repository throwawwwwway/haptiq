import threading
import time
import tkinter as tk
import conf

from pattern import Oscilate
from network import NetworkBehavior, Behavior, Node
from raw import Raw, Point, Actuator


def init_raw():
    conf.logger.info('Init raw')
    north = Actuator(90, 'North')
    est = Actuator(0, 'Est')
    south = Actuator(270, 'South')
    west = Actuator(180, 'West')
    return Raw([north, est, south, west])


def motion(event, raw):
    x, y = event.x, event.y
    raw.set_position(Point(x, y))


def haptiq_simulator(raw):
    root = tk.Tk()  # Launch panel
    root.bind('<Motion>', lambda event, raw=raw: motion(event, raw))
    root.mainloop()


def network_behavior(raw):
    center_node = Node(Point(50, 50))
    center_behavior = Behavior(center_node, Oscilate(), 10)
    net_behavior = NetworkBehavior([center_behavior])
    while 1:
        net_behavior.trigger_on(raw)
        time.sleep(3)

raw = init_raw()

simu = threading.Thread(target=network_behavior, args=(raw,))
simu.start()

haptiq_simulator(raw)
