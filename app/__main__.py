import threading
import time
import socket
import app.conf as conf

from app.network import Network, Node, Link
from app.raw import Raw, Actuator, Button
# from app.simulator import HaptiqSimulator
from app.view import HaptiqView
from app.tuio import TuioServer
from app.handler import PointsHandler


UDP_IP = "192.168.43.224"
UDP_PORT = 2390


def init_raw_4():
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


def labyrinth_network(raw):
    base_x = 100
    base_y = 150
    node_a = Node(base_x, base_y)
    node_b = Node(base_x * 2, base_y)
    node_c = Node(base_x * 2, base_y * 2)
    node_d = Node(base_x, base_y * 2)
    node_e = Node(base_x * 3, base_y)
    node_f = Node(base_x * 4, base_y * 2)
    node_g = Node(base_x * 3, base_y * 3)
    node_h = Node(base_x * 4, base_y * 3)
    node_i = Node(base_x * 5, base_y * 3)

    links = [
        Link(node_a, node_b),
        Link(node_b, node_c),
        Link(node_d, node_c),
        Link(node_e, node_c),
        Link(node_b, node_e),
        Link(node_e, node_f),
        Link(node_f, node_g),
        Link(node_h, node_f),
        Link(node_h, node_g),
        Link(node_h, node_i)
    ]
    return Network(
        [
            node_a, node_b, node_c, node_d,
            node_e, node_f, node_g, node_h, node_i
        ],
        links,
        raw
    )


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


def tracker(raw):
    handler = PointsHandler(raw, 1)
    server = TuioServer("0.0.0.0", 3333, handler)
    server.start()


def controller(raw):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while 1:
        for act in enumerate(raw.actuators):
            msg = "{} {}".format(str(act[0]), str(act[1].level))
            sock.sendto(bytes(msg, 'UTF-8'), (UDP_IP, UDP_PORT))
        time.sleep(0.5)

if __name__ == "__main__":
    raw = init_raw_4()    # Get the instance of our raw interface
    network = triangle_network(raw)

    # Launch the network behavior and the tuio server in separate threads
    behavior_thread = threading.Thread(
        target=network_behavior, args=(raw, network,))
    tracker_thread = threading.Thread(target=tracker, args=(raw,))
    controller_thread = threading.Thread(target=controller, args=(raw,))

    behavior_thread.start()
    # tracker_thread.start()
    controller_thread.start()
    tracker_thread.start()

    HaptiqView(raw, network)
