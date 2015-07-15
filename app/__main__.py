import threading
import time


import app.datasets as data
from app.device import Device
from app.view import View
from app.tuio import TuioServer
from app.handler import Handler
from app.interactions import DefaultInteract


def tracker(device, type=None):
    handler = Handler(device)
    server = TuioServer("0.0.0.0", 3333, handler)
    server.start()


def interact(view):
    current = DefaultInteract()
    while True:
        if current == view.interaction:
            current.process()
        else:
            current.close()
            current = DefaultInteract()
            if view.interaction is not None and view.interaction.open():
                current = view.interaction
            else:
                time.sleep(2)


if __name__ == "__main__":

    DefaultInteract.SIMULATION = True

    device = Device(data.actuators_8())

    # Initialising view with networks, interactions and mouse tracking
    view = View(
        device,
        networks=data.all_networks(),
        interacts=data.all_interactions(),
        mouse_tracking=False,
        default_network='triangle',
        default_interact='HaptiQ_complex_guidance'
    )

    # Setting tracking and interacting threadq
    tracker_thrd = threading.Thread(target=tracker, args=(device,))
    interaction_thrd = threading.Thread(target=interact, args=(view,))

    # Starting threads
    # tracker_thrd.start()
    interaction_thrd.start()

    view.loop()  # runs the view, forever
