import tkinter as tk
import app.conf as cf

from tkinter import Canvas, Menu
from app.raw import Point
from app.network import Node, Link
from functools import partial


def motion(event, raw):
    x, y = event.x, event.y
    raw.position = Point(x, y)


def color_from_level(level):
    '''return a hex black depth color depending on the level'''
    intensity = 255 - int(level * 2.55) % 256
    return '#%02x%02x%02x' % (intensity, intensity, intensity)


class HaptiqView(object):

    def __init__(self, raw, networks=None, mouse_tracking=False):
        self.root = tk.Tk()
        self.networks = networks

        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        for key, network in networks.items():
            network.raw = raw
            partial_command = partial(self.load_network, key)
            filemenu.add_command(
                label=key, command=partial_command)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_exit)

        self.scene = Scene(self.root, raw, mouse_tracking)
        self.load_network(next(iter(networks)))

    def loop(self):
        self.root.mainloop()

    def load_network(self, network_key):
        print("load_network called with: " + str(network_key))
        self.network = self.networks[network_key]
        self.scene.draw_network(self.network)

    def current_network(self):
        return self.network

    def on_exit(self):
        self.root.destroy()


class Scene(object):
    def __init__(self, master, raw, mouse_tracking=False):
        self.master = master
        self.raw = raw
        self.frame = tk.Frame(self.master)
        self.buttonFeedback = tk.Button(
            self.frame,
            text="Feedback window",
            width=25,
            command=self.open_feedback
        )
        self.buttonFeedback.pack()
        self.explore_canvas = Canvas(master, width=500, height=500)
        self.explore_canvas.pack()

        if mouse_tracking:
            self.explore_canvas.bind(
                '<Motion>', lambda event, raw=raw: motion(event, raw))

        self.enable_position_feedback()
        self.network_drawings = []

        self.frame.pack()
        self.app = None
        self.update()

    def enable_position_feedback(self):
        self.device_cursor = self.explore_canvas.create_oval(
            self.raw.position.x - 2.5, self.raw.position.y - 2.5,
            self.raw.position.x + 2.5, self.raw.position.y + 2.5)

    def draw_network(self, network):
        self.explore_canvas.delete('all')
        self.enable_position_feedback()
        for elem in network.elems:
            if type(elem) is Node:
                pos_x = elem.x - 5
                pos_y = elem.y - 5
                self.explore_canvas.create_oval(
                    pos_x, pos_y, pos_x + 10, pos_y + 10, fill="blue")
            elif type(elem) is Link:
                pt_a = elem.first
                pt_b = elem.sec
                self.explore_canvas.create_line(
                    pt_a.x, pt_a.y, pt_b.x, pt_b.y)

    def update(self):
        coords = self.explore_canvas.coords(self.device_cursor)
        if len(coords) <= 3:
            self.master.after(50, self.update)
            return
        center = ((coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2)
        self.explore_canvas.move(
            self.device_cursor,
            self.raw.position.x - center[0],
            self.raw.position.y - center[1])
        if self.app and not self.app.closed:
            self.app.update()
        self.master.after(50, self.update)

    def open_feedback(self):
        self.feedbackWindow = tk.Toplevel(self.master)
        self.app = Feedback(self.feedbackWindow, self.raw)


class Feedback(object):

    def __init__(self, master, raw):
        self.master = master
        self.raw = raw
        self.frame = tk.Frame(master)
        self.on_update = False
        self.mapped_actuators = {}

        self.quitButton = tk.Button(
            self.frame, text='Quit', width=25, command=self.close_window)
        self.quitButton.pack()
        self.master.protocol("WM_DELETE_WINDOW", self.close_window)

        self.canvas = Canvas(master, width=250, height=250)
        self.canvas.pack()
        self.set_mapping()
        cf.logger.debug("Raw actuators: {}".format(self.raw.actuators))

        self.frame.pack()
        self.closed = False

    def set_mapping(self):
        cntr_x = 250 / 2
        cntr_y = 250 / 2
        straight = 90
        wd = 8

        self.north = self.canvas.create_line(
            cntr_x, cntr_y - 8, cntr_x, cntr_y - straight, width=wd)
        self.east = self.canvas.create_line(
            cntr_x + 8, cntr_y, cntr_x + straight, cntr_y, width=wd)
        self.south = self.canvas.create_line(
            cntr_x, cntr_y + 8, cntr_x, cntr_y + straight, width=wd)
        self.west = self.canvas.create_line(
            cntr_x - 8, cntr_y, cntr_x - straight, cntr_y, width=wd)

        if len(self.raw.actuators) == 8:
            diag = straight * 0.75
            self.north_east = self.canvas.create_line(
                cntr_x + 8, cntr_y - 8, cntr_x + diag, cntr_y - diag, width=wd)
            self.south_east = self.canvas.create_line(
                cntr_x + 8, cntr_y + 8, cntr_x + diag, cntr_y + diag, width=wd)
            self.south_west = self.canvas.create_line(
                cntr_x - 8, cntr_y + 8, cntr_x - diag, cntr_y + diag, width=wd)
            self.north_west = self.canvas.create_line(
                cntr_x - 8, cntr_y - 8, cntr_x - diag, cntr_y - diag, width=wd)
            self.mapped_actuators = {
                self.raw.actuators[0]: self.east,
                self.raw.actuators[1]: self.north_east,
                self.raw.actuators[2]: self.north,
                self.raw.actuators[3]: self.north_west,
                self.raw.actuators[4]: self.west,
                self.raw.actuators[5]: self.south_west,
                self.raw.actuators[6]: self.south,
                self.raw.actuators[7]: self.south_east
            }
        else:
            self.mapped_actuators = {
                self.raw.actuators[0]: self.east,
                self.raw.actuators[1]: self.north,
                self.raw.actuators[2]: self.west,
                self.raw.actuators[3]: self.south,
            }

        if self.raw.button is not None:
            self.center = self.canvas.create_oval(
                cntr_x - 10, cntr_y - 10, cntr_x + 10, cntr_y + 10)
            self.mapped_actuators[self.raw.button] = self.center

    def update(self):
        for actuator in self.mapped_actuators:
            # cf.logger.debug("updating actuator {}".format(actuator.level))
            self.canvas.itemconfig(
                self.mapped_actuators[actuator],
                fill=color_from_level(actuator.level))

    def close_window(self):
        self.closed = True
        self.master.destroy()
