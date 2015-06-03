import threading
import time
import socket
import app.conf as conf

from app.network import Network, Node, Link
from app.raw import Raw, Actuator, Button
# from app.simulator import HaptiqSimulator
from app.view import HaptiqView
from app.tuio import TuioServer
from app.handler import Handler


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


def exp1_network(raw):
    home = Node(5, 8)
    cinema = Node(8, 7)
    police = Node(7, 3)
    market = Node(14, 5)
    city_hall = Node(15, 10)
    school = Node(7, 12)
    tower = Node(3, 15)

    links = [
        Link(home, cinema),
        Link(home, police),
        Link(cinema, police),
        Link(police, market),
        Link(market, city_hall),
        Link(school, city_hall),
        Link(home, school)
    ]

    return Network(
        [home, cinema, police, market, city_hall, school, tower],
        links,
        raw
    )


def conc1_network(raw):
    sophie = Node(6, 2)
    mathiew = Node(2, 6)
    jean = Node(10, 6)
    martin = Node(2, 10)
    harold = Node(10, 10)
    helene = Node(14, 10)
    julie = Node(10, 14)
    marie = Node(14, 14)

    links = [
        Link(sophie, mathiew),
        Link(sophie, jean),
        Link(jean, mathiew),
        Link(martin, mathiew),
        Link(jean, harold),
        Link(jean, helene),
        Link(mathiew, harold),
        Link(harold, julie),
        Link(helene, marie),
        Link(julie, marie)
    ]
    return Network(
        [sophie, mathiew, jean, martin, harold, helene, julie, marie],
        links,
        raw
    )


def labyrinth_network(raw):
    node_a = Node(1, 1)
    node_b = Node(2, 1)
    node_c = Node(2, 2)
    node_d = Node(1, 2)
    node_e = Node(3, 1)
    node_f = Node(4, 2)
    node_g = Node(3, 3)
    node_h = Node(4, 3)
    node_i = Node(5, 3)

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
    node_a = Node(1, 1)
    node_b = Node(4, 2)
    node_c = Node(2, 4)
    node_e = Node(2, 2)
    node_f = Node(4.5, 4.5)

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
        network.update_behaviors()
        network.apply_behaviors()
        time.sleep(0.1)


def tracker(raw, type=None):
    handler = Handler(raw)
    server = TuioServer("0.0.0.0", 3333, handler)
    server.start()


def controller(raw):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while 1:
        for act in enumerate(raw.actuators):
            if act[1].should_update():
                msg = "{} {}".format(str(act[0]), str(act[1].level))
                sock.sendto(bytes(msg, 'UTF-8'), (UDP_IP, UDP_PORT))
        time.sleep(0.1)

if __name__ == "__main__":
    raw = init_raw_9()    # Get the instance of our raw interface
    network = triangle_network(raw)
    #  network = exp1_network(raw)
    # network = conc1_network(raw)

    # Launch the network behavior and the tuio server in separate threads
    behavior_thread = threading.Thread(
        target=network_behavior, args=(raw, network,))
    tracker_thread = threading.Thread(target=tracker, args=(raw,))
    controller_thread = threading.Thread(target=controller, args=(raw,))

    behavior_thread.start()
    tracker_thread.start()
    controller_thread.start()
    # tracker_thread.start()

    HaptiqView(raw, network, False)  # Last argument is for tracking the mouse
