import threading
import time
import conf
# import sys
# import signal

from pattern import Oscilate
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


def network_behavior(raw):
    center_node = Node(Point(50, 50))
    center_behavior = Behavior(center_node, Oscilate(), 10)
    net_behavior = NetworkBehavior([center_behavior])
    while 1:
        net_behavior.trigger_on(raw)
        time.sleep(1)


raw = init_raw()    # Get the instance of our raw interface

# Launch the network behavior in another thread
simu = threading.Thread(target=network_behavior, args=(raw,))
simu.start()

# Launch the simulator in the current thread
HaptiqSimulator(raw)
