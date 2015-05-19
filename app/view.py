import tkinter as tk
import app.conf as cf

from tkinter import Canvas
from app.raw import Point


def motion(event, raw):
    x, y = event.x, event.y
    raw.position = Point(x, y)


def color_from_level(level):
    '''return a hex black depth color depending on the level'''
    intensity = 255 - int(level * 2.55) % 256
    return '#%02x%02x%02x' % (intensity, intensity, intensity)


class HaptiqView(object):
    def __init__(self, raw, network=None):
        root = tk.Tk()
        Scene(root, raw, network)
        root.mainloop()


class Scene(object):
    def __init__(self, master, raw, network=None):
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

        if (network is not None):  # let's draw
            for node in list(network.nodes_behavior.keys()):
                pos_x = node.x - 5
                pos_y = node.y - 5
                self.explore_canvas.create_oval(
                    pos_x, pos_y, pos_x + 10, pos_y + 10, fill="blue")
            for link in list(network.links_behavior.keys()):
                pt_a = link.first
                pt_b = link.sec
                self.explore_canvas.create_line(
                    pt_a.x, pt_a.y, pt_b.x, pt_b.y)

        # self.explore_canvas.bind(
        #     '<Motion>', lambda event, raw=raw: motion(event, raw))

        self.device_cursor = self.explore_canvas.create_oval(
            0, 0, 5, 5)

        self.frame.pack()
        self.previous = Point(0, 0)
        self.app = None
        self.update()

    def update(self):
        self.explore_canvas.move(
            self.device_cursor,
            self.raw.position.x - self.previous.x,
            self.raw.position.y - self.previous.y)
        self.previous = self.raw.position
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
            cf.logger.info("updating actuator {}".format(actuator.level))
            self.canvas.itemconfig(
                self.mapped_actuators[actuator],
                fill=color_from_level(actuator.level))

    def close_window(self):
        self.closed = True
        self.master.destroy()
