import tkinter as tk
import app.logconfig as lc

from tkinter import Canvas, Menu
from app.device import Point
from functools import partial
from app.network import Network


def motion(event, device):
    x, y = event.x, event.y
    device.position = Point(x, y)


def color_from_level(level):
    '''return a hex black depth color depending on the level'''
    intensity = 255 - int(level * 2.55) % 256
    return '#%02x%02x%02x' % (intensity, intensity, intensity)


class View(object):

    def __init__(self, device, **opts):

        self.root = tk.Tk()
        self.networks = opts['networks'] if 'networks' in opts else []
        self.interacts = opts['interacts'] if 'interacts' in opts else []

        self._network = None
        self._interaction = None

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        if self.networks != []:
            newtwork_menu = Menu(menubar)
            menubar.add_cascade(label="Networks", menu=newtwork_menu)
            for key, network in sorted(self.networks.items()):
                partial_command = partial(self.load_network, key)
                newtwork_menu.add_command(
                    label=key, command=partial_command)

        if self.interacts != []:
            interaction_menu = Menu(menubar)
            menubar.add_cascade(label="Interactions", menu=interaction_menu)
            for key, interaction in sorted(self.interacts.items()):
                interaction.device = device
                interaction.view = self
                partial_command = partial(
                    self.load_interaction, key)
                interaction_menu.add_command(
                    label=key, command=partial_command)
        mouse_tracking = opts['mouse_tracking'] if 'mouse_tracking' in opts else False
        self.scene = Scene(self.root, device, mouse_tracking)
        if 'default_network' in opts:
            self.load_network(opts['default_network'])
        if 'default_interact' in opts:
            self.load_interaction(opts['default_interact'])

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, value):
        self._network = value
        self.scene.draw_network(value)
        lc.log.info(str(value))

    def load_network(self, key):
        lc.log.info("network: {}".format(key))
        if (key[:3] == 'gen'):
            print(key[4])
            self.network = Network.generate(int(key[4]))
        else:
            self.network = self.networks[key]

    @property
    def interaction(self):
        return self._interaction

    @interaction.setter
    def interaction(self, value):
        self._interaction = value

    def load_interaction(self, key):
        lc.log.info("interaction: {}".format(key))
        self.interaction = self.interacts[key]

    def on_exit(self):
        self.root.destroy()

    def loop(self):
        self.root.mainloop()


class Scene(object):
    def __init__(self, master, device, mouse_tracking=False):
        self.master = master
        self.device = device
        self.frame = tk.Frame(self.master)
        self.feedbackButton = tk.Button(
            self.frame,
            text="Feedback window",
            width=25,
            command=self.open_feedback
        )
        self.feedbackButton.pack()
        self.explore_canvas = Canvas(master, width=500, height=500)
        self.explore_canvas.pack()

        if mouse_tracking:
            self.explore_canvas.bind(
                '<Motion>', lambda event, device=device: motion(event, device))

        self.enable_position_feedback()
        self.network_drawings = []

        self.frame.pack()
        self.app = None
        self.update()

    def enable_position_feedback(self):
        self.device_cursor = self.explore_canvas.create_oval(
            self.device.position.x - 2.5, self.device.position.y - 2.5,
            self.device.position.x + 2.5, self.device.position.y + 2.5)

    def draw_network(self, network):
        self.explore_canvas.delete('all')
        self.enable_position_feedback()
        for node in network.nodes:
            pos_x = node.x - 5
            pos_y = node.y - 5
            self.explore_canvas.create_oval(
                pos_x, pos_y, pos_x + 10, pos_y + 10, fill="blue")
        for link in network.links:
            pt_a = link.first
            pt_b = link.sec
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
            self.device.position.x - center[0],
            self.device.position.y - center[1])
        if self.app and not self.app.closed:
            self.app.update()
        self.master.after(50, self.update)

    def open_feedback(self):
        self.feedbackWindow = tk.Toplevel(self.master)
        self.app = Feedback(self.feedbackWindow, self.device)


class Feedback(object):

    def __init__(self, master, device):
        self.master = master
        self.device = device
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
        lc.log.debug("device actuators: {}".format(self.device.actuators))

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

        if len(self.device.actuators) == 8:
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
                self.device.actuators[0]: self.east,
                self.device.actuators[1]: self.north_east,
                self.device.actuators[2]: self.north,
                self.device.actuators[3]: self.north_west,
                self.device.actuators[4]: self.west,
                self.device.actuators[5]: self.south_west,
                self.device.actuators[6]: self.south,
                self.device.actuators[7]: self.south_east
            }
        else:
            self.mapped_actuators = {
                self.device.actuators[0]: self.east,
                self.device.actuators[1]: self.north,
                self.device.actuators[2]: self.west,
                self.device.actuators[3]: self.south,
            }

    def update(self):
        for actuator in self.mapped_actuators:
            self.canvas.itemconfig(
                self.mapped_actuators[actuator],
                fill=color_from_level(actuator.level))

    def close_window(self):
        self.closed = True
        self.master.destroy()
