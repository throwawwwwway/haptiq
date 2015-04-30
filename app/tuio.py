import argparse

from pythonosc import dispatcher
from pythonosc import osc_server


def interpret_2Dcur(*args):  # noqa
    handler = args[1][0]
    if args[2] == 'set':
        cur_id = args[3]
        handler.manage(cur_id, args[4], args[5])


class TuioServer(object):

    def __init__(self, address="0.0.0.0", port=3333, handler=None):

        self.handler = handler
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default=address)
        parser.add_argument("--port", type=int, default=port)
        args = parser.parse_args()

        disp = dispatcher.Dispatcher()
        disp.map("/tuio/2Dcur", interpret_2Dcur, self.handler)

        self.server = osc_server.ThreadingOSCUDPServer(
            (args.ip, args.port), disp)
        print("Serving on {}".format(self.server.server_address))

    def start(self):
        self.server.serve_forever()
