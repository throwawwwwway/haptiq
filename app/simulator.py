import tkinter as tk
import conf
from tkinter import Canvas
from raw import Point


def motion(event, raw):
    x, y = event.x, event.y
    raw.set_position(Point(x, y))


def color_from_level(level):
    factor = level * 255 / 100
    return '#%02x%02x%02x' % (factor, 250, 255 - factor)


class HaptiqSimulator(object):

    def __init__(self, raw):
        root = tk.Tk()
        self.exploration = Explore(root, raw)
        root.mainloop()


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
        self.app = Feedback(self.newWindow, self.raw)

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
        self.button2 = tk.Button(
            self.frame, text='Update', width=25, command=self.update_simulator)
        self.button2.pack()

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

    def update_simulator(self):
        conf.logger.info("Updating simulator")
        self.canvas.itemconfig(
            self.north, fill=color_from_level(self.raw.get_level('North')))
        self.canvas.itemconfig(
            self.east, fill=color_from_level(self.raw.get_level('East')))
        self.canvas.itemconfig(
            self.south, fill=color_from_level(self.raw.get_level('South')))
        self.canvas.itemconfig(
            self.west, fill=color_from_level(self.raw.get_level('West')))

    def close_windows(self):
        self.master.destroy()
