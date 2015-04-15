import tkinter as tk
# import conf as cf

from tkinter import Canvas
from raw import Point


def motion(event, raw):
    x, y = event.x, event.y
    raw.position = Point(x, y)


def color_from_level(level):
    '''return a hex blue depth color depending on the level'''
    intensity = 255 - int(level * 2.55) % 256
    return '#%02x%02x%02x' % (intensity, intensity, intensity)


class HaptiqSimulator(object):

    def __init__(self, raw, network=None):
        root = tk.Tk()
        Explore(root, raw, network)
        root.mainloop()


class Explore(object):
    def __init__(self, master, raw, network=None):
        self.master = master
        self.raw = raw
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(
            self.frame, text='Open view', width=25, command=self.new_window)
        self.button1.pack()

        self.explore_canvas = Canvas(master, width=500, height=500)
        self.explore_canvas.pack()

        if (network is not None and False):  # let's draw
            for node in network.nodes:
                pos_x = node.point.x - 5
                pos_y = node.point.y - 5
                self.explore_canvas.create_oval(
                    pos_x, pos_y, pos_x + 10, pos_y + 10, fill="blue")

        self.explore_canvas.bind(
            '<Motion>', lambda event, raw=raw: motion(event, raw))

        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        app = Feedback(self.newWindow, self.raw)
        app.update()

    def update(self):
        pass


class Feedback(object):

    def __init__(self, master, raw):
        self.master = master
        self.raw = raw
        self.frame = tk.Frame(master)
        self.on_update = False
        self.mapped_actuators = {}

        self.quitButton = tk.Button(
            self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()

        self.canvas = Canvas(master, width=250, height=250)
        self.canvas.pack()
        cntr_x = 250 / 2
        cntr_y = 250 / 2
        straight = 90
        # diag = straight * 0.75
        width = 8
        self.north = self.canvas.create_line(
            cntr_x, cntr_y - 8, cntr_x, cntr_y - straight, width=width)
        self.east = self.canvas.create_line(
            cntr_x + 8, cntr_y, cntr_x + straight, cntr_y, width=width)
        self.south = self.canvas.create_line(
            cntr_x, cntr_y + 8, cntr_x, cntr_y + straight, width=width)
        self.west = self.canvas.create_line(
            cntr_x - 8, cntr_y, cntr_x - straight, cntr_y, width=width)

        self.mapped_actuators = {
            self.raw.actuators[0]: self.east,
            self.raw.actuators[1]: self.north,
            self.raw.actuators[2]: self.west,
            self.raw.actuators[3]: self.south
        }
        # self.north_east = self.canvas.create_line(
        #     cntr_x + 8, cntr_y - 8, cntr_x + diag,cntr_y - diag, width=width)
        # self.south_east = self.canvas.create_line(
        #     cntr_x + 8, cntr_y + 8, cntr_x + diag,cntr_y + diag, width=width)
        # self.south_west = self.canvas.create_line(
        #     cntr_x - 8, cntr_y + 8, cntr_x - diag,cntr_y + diag, width=width)
        # self.north_west = self.canvas.create_line(
        #     cntr_x - 8, cntr_y - 8, cntr_x - diag,cntr_y - diag, width=width)

        self.frame.pack()

    def update(self):
        for actuator in self.mapped_actuators:
            self.canvas.itemconfig(
                self.mapped_actuators[actuator],
                fill=color_from_level(self.raw.get_level(actuator)))

        self.master.after(50, self.update)

    def close_windows(self):
        self.master.destroy()
