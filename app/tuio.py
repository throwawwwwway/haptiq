import argparse
import app.logconfig as lc

from pythonosc import dispatcher
from pythonosc import osc_server
from app.handler import Handler
from app.device import Device
from app.network import Point


def interpret_2Dcur(*args):  # noqa
    """
        0: '/tui/2Dcur'
        1: <handler object>
        2: {set, alive, ...}
        3: <2Dcur id>
        4: x pos
        5: y pos
        6: X direction
        7 : Y direction
    """
    handler = args[1][0]
    if args[2] == 'alive':
        points = []
        i = 3
        while i < len(args):
            points.append(args[i])
            i += 1
        handler.manage(points)
    elif args[2] == 'set':
        handler.points[args[3]] = Point(args[4], args[5])
    elif args[2] == 'fseq':
        handler.update_device()


class TuioServer(object):

    def __init__(self, address="0.0.0.0", port=3333, handler=None):
        self.handler = handler
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=address)
        parser.add_argument("--port", type=int, default=port)
        args = parser.parse_args()

        disp = dispatcher.Dispatcher()
        disp.map("/tuio/2Dcur", interpret_2Dcur, self.handler)

        self.server = None
        try:
            self.server = osc_server.ThreadingOSCUDPServer(
                (args.ip, args.port), disp)
            lc.log.debug("Serving on {}".format(self.server.server_address))
        except:
            lc.log.warning("Cannot listen on port 3333. Is port used?")

    def start(self):
        if self.server is not None:
            self.server.serve_forever()


if __name__ == '__main__':
    points_handler = Handler(Device())
    tuio = TuioServer("0.0.0.0", 3333, points_handler)
    lc.log.debug("Tuio Server launched")
    tuio.start()
