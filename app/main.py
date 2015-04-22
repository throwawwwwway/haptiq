import threading
import time
import conf

from network import Network, Node, Link
from raw import Raw, Actuator
from simulator import HaptiqSimulator


def init_raw():
    conf.logger.info('Init raw')
    north = Actuator(90, 'North')
    east = Actuator(0, 'East')
    south = Actuator(270, 'South')
    west = Actuator(180, 'West')
    # north_east = Actuator(45, 'North-East')
    # north_west = Actuator(135, 'North-West')
    # south_west = Actuator(225, 'South-West')
    # south_east = Actuator(315, 'South-East')
    return Raw([east, north, west, south])


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


raw = init_raw()    # Get the instance of our raw interface

# network = triangle_network(raw)
# network = test_network_one_point(raw)
network = test_network_two_points(raw)

# Launch the network behavior in another thread
network_thread = threading.Thread(
    target=network_behavior, args=(raw, network,))
network_thread.start()

HaptiqSimulator(raw, network)  # Launch the simulator in the current thread
