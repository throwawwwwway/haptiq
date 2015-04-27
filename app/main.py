import threading
import time
import conf
import sys
import liblo

from network import Network, Node, Link, Point
from raw import Raw, Actuator, Button
from simulator import HaptiqSimulator
from py3tuio.main import TuioServer


def init_raw():
    conf.logger.info('Init raw')
    east = Actuator(0, 'East')
    north = Actuator(90, 'North')
    west = Actuator(180, 'West')
    south = Actuator(270, 'South')
    return Raw([east, north, west, south])


def init_raw_8():
    conf.logger.info('Init raw 8 Actuators')
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
    conf.logger.info('Init raw 8 Actuators')
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


def triangle_network(raw):
    node_a = Node(100, 100)
    node_b = Node(400, 200)
    node_c = Node(200, 400)
    node_e = Node(200, 200)
    node_f = Node(450, 450)

    link_1 = Link(node_a, node_b)
    link_2 = Link(node_b, node_c)
    link_3 = Link(node_c, node_a)

    return Network(
        [node_a, node_b, node_c, node_e, node_f],
        [link_1, link_2, link_3],
        raw
    )


def test_network_one_point(raw):
    return Network([Node(250, 250)], [], raw)


def test_network_two_points(raw):
    return Network(
        [Node(200, 200), Node(250, 250)], [], raw)


def network_behavior(raw, network):
    while 1:
        if raw.mouse_moved:
            network.update_behaviors()
        network.apply_behaviors()
        time.sleep(0.1)


def tuio(raw):
    try:
        server = TuioServer(8080)
    except liblo.ServerError as err:
        sys.exit(str(err))
    server.start()
    while (True):
        time.sleep(0.1)
        try:
            cursor = server.main_cursor()
            if cursor is not None:
                print("Cursor is at ({}, {})".format(
                    str(cursor.x * 500), str(cursor.y * 500)))
                raw.position = Point(cursor.x * 500, cursor.y * 500)
        except:
            server.stop()
            raise


raw = init_raw_9()    # Get the instance of our raw interface

network = triangle_network(raw)
# network = test_network_one_point(raw)
# network = test_network_two_points(raw)

# Launch the network behavior in another thread
network_thread = threading.Thread(
    target=network_behavior, args=(raw, network,))
tuio_thread = threading.Thread(target=tuio, args=(raw,))

network_thread.start()
tuio_thread.start()

HaptiqSimulator(raw, network)  # Launch the simulator in the current thread
