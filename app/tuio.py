import argparse

from pythonosc import dispatcher
from pythonosc import osc_server


def print_2dcur(unused_addr, *args):  # noqa
    for arg in args:
        print("{}".format(str(arg)))


class TuioServer(object):

    def __init__(self, address="0.0.0.0", port=3333, raw=None):
        self.raw = raw
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=address)
        parser.add_argument("--port", type=int, default=port)
        args = parser.parse_args()

        disp = dispatcher.Dispatcher()
        disp.map("/tuio/2Dcur", self.compute_2Dcurr, "2Dcur")

        self.server = osc_server.ThreadingOSCUDPServer(
            (args.ip, args.port), disp)
        print("Serving on {}".format(self.server.server_address))

    def compute_2Dcur(self, *args):  # noqa
        for arg in args:
            print("{}".format(str(arg)))

    def start(self):
        self.server.serve_forever()
