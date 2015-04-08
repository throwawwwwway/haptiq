import tkinter as tk
import conf
from tkinter import Canvas
from raw import Point

color_classes = ["#fff", "#ffffcc", "#ffeda0", "#fed976", "#feb24c", "#fd8d3c", "#fc4e2a", "#e31a1c", "#bd0026", "#800026"]


def motion(event, raw):
    x, y = event.x, event.y
    raw.set_position(Point(x, y))


def color_from_level(level):
    if level > 99:
        level = 99
        conf.logger.warning("Bad level: {}".format(level))
    return color_classes[int(level / 10)]


class HaptiqSimulator(object):

    def __init__(self, raw):
        self.root = tk.Tk()
        self.exploration = Explore(self.root, raw)

    def loop(self):
        self.root.mainloop()


class Explore(object):
    def __init__(self, master, raw):
        self.master = master
        self.raw = raw
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(
            self.frame, text='Open view', width=25, command=self.new_window)
        self.button1.pack()

        self.explore_canvas = Canvas(master, width=500, height=500)
        self.explore_canvas.pack()
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

        self.quitButton = tk.Button(
            self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()

        self.canvas = Canvas(master, width=250, height=250)
        self.canvas.pack()
        cntr_x = 250 / 2
        cntr_y = 250 / 2
        straight = 90
        diag = straight * 0.75
        width = 8
        self.north = self.canvas.create_line(
            cntr_x, cntr_y - 8, cntr_x, cntr_y - straight, width=width)
        self.north_east = self.canvas.create_line(
            cntr_x + 8, cntr_y - 8, cntr_x + diag, cntr_y - diag, width=width)
        self.east = self.canvas.create_line(
            cntr_x + 8, cntr_y, cntr_x + straight, cntr_y, width=width)
        self.south_east = self.canvas.create_line(
            cntr_x + 8, cntr_y + 8, cntr_x + diag, cntr_y + diag, width=width)
        self.south = self.canvas.create_line(
            cntr_x, cntr_y + 8, cntr_x, cntr_y + straight, width=width)
        self.south_west = self.canvas.create_line(
            cntr_x - 8, cntr_y + 8, cntr_x - diag, cntr_y + diag, width=width)
        self.west = self.canvas.create_line(
            cntr_x - 8, cntr_y, cntr_x - straight, cntr_y, width=width)
        self.north_west = self.canvas.create_line(
            cntr_x - 8, cntr_y - 8, cntr_x - diag, cntr_y - diag, width=width)

        self.frame.pack()

    def update(self):
        conf.logger.info("Updating simulator")
        self.canvas.itemconfig(
            self.north, fill=color_from_level(self.raw.get_level('North')))
        self.canvas.itemconfig(
            self.east, fill=color_from_level(self.raw.get_level('East')))
        self.canvas.itemconfig(
            self.south, fill=color_from_level(self.raw.get_level('South')))
        self.canvas.itemconfig(
            self.west, fill=color_from_level(self.raw.get_level('West')))
        self.master.after(100, self.update)

    def close_windows(self):
        self.master.destroy()
