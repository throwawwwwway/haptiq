import threading
import time
import conf
# import sys
# import signal

from pattern import Pattern, Oscilate
from network import NetworkBehavior, Behavior, Node
from raw import Raw, Point, Actuator
from simulator import HaptiqSimulator


def init_raw():
    conf.logger.info('Init raw')
    north = Actuator(90, 'North')
    est = Actuator(0, 'East')
    south = Actuator(270, 'South')
    west = Actuator(180, 'West')
    return Raw([north, est, south, west])


def simple_point():
    center_node = Node(Point(50, 50))
    center_behavior = Behavior(center_node, Oscilate(), 10)
    net_behavior = NetworkBehavior([center_behavior])
    return net_behavior


def cool_network():
    bhs = []
    weak = Pattern([50, 0])
    strong = Pattern([90])

    nodes = []
    nodes.append(Node(Point(20, 30), [90, 0, 270]))
    nodes.append(Node(Point(50, 10), [180, 270, 0]))
    nodes.append(Node(Point(80, 30), [90, 180, 270]))
    nodes.append(Node(Point(50, 50), [0, 90, 180]))
    nodes.append(Node(Point(80, 80), [90, 180, 270]))
    nodes.append(Node(Point(50, 100), [0, 90, 180]))
    nodes.append(Node(Point(20, 80), [0, 270]))

    for node in nodes:
        bhs.append(Behavior(node, weak, 10))
        bhs.append(Behavior(node, strong, 5))

    return NetworkBehavior(bhs)


def network_behavior(raw, network):
    while 1:
        net_behavior.trigger_on(raw)
        time.sleep(0.1)


raw = init_raw()    # Get the instance of our raw interface


net_behavior = cool_network()

# Launch the network behavior in another thread
network_behavior = threading.Thread(
    target=network_behavior, args=(raw, net_behavior,))
network_behavior.start()

HaptiqSimulator(raw)  # Launch the simulator in the current thread
