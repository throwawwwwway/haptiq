import threading
import time
import socket
import serial
import os.path

import app.conf as cf
import app.networkdata as ndata
from app.raw import Raw, Actuator, Button
from app.view import HaptiqView
from app.tuio import TuioServer
from app.handler import Handler


UDP_IP = "192.168.43.224"
UDP_PORT = 2390

# SERIAL_PATH = '/dev/tty.usbmodem1411'
SERIAL_PATH = '/dev/cu.HC-06-DevB'


def init_raw_4():
    cf.logger.info('Init raw')
    east = Actuator(0, 'East')
    north = Actuator(90, 'North')
    west = Actuator(180, 'West')
    south = Actuator(270, 'South')
    return Raw([east, north, west, south])


def init_raw_8():
    cf.logger.info('Init raw 8 Actuators')
    east = Actuator(0, 'East')
    north_east = Actuator(45, 'North-East')
    north = Actuator(90, 'North')
    north_west = Actuator(135, 'North-West')
    west = Actuator(180, 'West')
    south_west = Actuator(225, 'South-West')
    south = Actuator(270, 'South')
    south_east = Actuator(315, 'South-East')
    return Raw([
        east, north_east, north, north_west,
        west, south_west, south, south_east])


def init_raw_9():
    cf.logger.info('Init raw 8 Actuators')
    east = Actuator(0, 'East')
    north_east = Actuator(45, 'North-East')
    north = Actuator(90, 'North')
    north_west = Actuator(135, 'North-West')
    west = Actuator(180, 'West')
    south_west = Actuator(225, 'South-West')
    south = Actuator(270, 'South')
    south_east = Actuator(315, 'South-East')
    button = Button('center')
    return Raw([
        east, north_east, north, north_west,
        west, south_west, south, south_east],
        button)


def behavior(raw, view):
    while 1:
        network = view.current_network()
        if network is not None:
            network.update_behaviors()
            network.apply_behaviors()
        time.sleep(0.1)


def tracker(raw, type=None):
    handler = Handler(raw)
    server = TuioServer("0.0.0.0", 3333, handler)
    server.start()


def controller_serial(raw):
    ser = serial.Serial(SERIAL_PATH, baudrate=115200, timeout=0)
    while True:
        time.sleep(0.1)
        for act in enumerate(raw.actuators):
            if act[1].should_update():
                cf.logger.debug("serial sent with: ({}, {})".format(
                    str(act[0]), str(act[1].level)))
                msg = 's{}{}f'.format(str(act[0]), str(act[1].level))
                ser.write(bytes(msg, 'UTF-8'))


def controller_udb(raw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        time.sleep(0.05)
        for act in enumerate(raw.actuators):
            if act[1].should_update():
                cf.logger.debug("udp sent with: ({}, {})".format(
                    str(act[0]), str(act[1].level)))
                msg = "{} {}".format(str(act[0]), str(act[1].level))
                sock.sendto(bytes(msg, 'UTF-8'), (UDP_IP, UDP_PORT))
                time.sleep(0.05)

if __name__ == "__main__":

    # Getting the raw instance
    raw = init_raw_9()

    # Getting/Setting the view with networks and tracking mouse
    view = HaptiqView(raw, ndata.all_networks(), False)

    # Setting the behavior trigger, the tracker and the device controller
    behavior_thread = threading.Thread(target=behavior, args=(raw, view,))
    tracker_thread = threading.Thread(target=tracker, args=(raw,))
    controller_thread = threading.Thread(target=controller_serial, args=(raw,))

    # threads starting
    behavior_thread.start()
    tracker_thread.start()
    controller_thread.start()

    view.loop()  # runs the view, forever
