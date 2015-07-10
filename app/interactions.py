import serial
import os

import app.logconfig as lc


class DefaultInteract(object):
    SIMULATION = False

    def __init__(self):
        self.device = None
        self.view = None

    def open(self):
        if self.device is None or self.view is None:
            lc.log.warning("device or network missing in interaction")
            print("device: {}, network: {}".format(
                self.device, self.view))
            return False

    def process(self):
        pass

    def close(self):
        pass


class HaptiQInteract(DefaultInteract):
    SERIAL_PATH = '/dev/cu.HC-06-DevB'

    def __init__(self):
        super().__init__()

    def open(self, simulation=False):
        super().open()
        if DefaultInteract.SIMULATION:
            return True
        lc.log.debug("Trying opening serial")
        try:
            self.ser = serial.Serial(
                HaptiQInteract.SERIAL_PATH, baudrate=115200, timeout=0)
        except:
            lc.log.warning("Cannot open serial communication.")
            return False
        return True

    def process(self, simulation=False):
        if DefaultInteract.SIMULATION:
            return True
        for act in enumerate(self.raw.actuators):
            if act[1].should_update():
                lc.log.debug("serial sent with: ({}, {})".format(
                    str(act[0]), str(act[1].level)))
                msg = 's{}{}f'.format(str(act[0]), str(act[1].level))
                self.ser.write(bytes(msg, 'UTF-8'))

    def close(self):
        self.ser.close()
        lc.log.debug("Closing HaptiQ interaction")


class VoiceInteract(DefaultInteract):
    def __init__(self):
        super().__init__()

    def open(self):
        super().open()
        self.last_guidance = None
        try:
            os.system("say -v Thomas \"Initialization\" &")
        except Exception as e:
            lc.log.warning("Cannot use 'say' command, (not on OSX?): ", e)
            return False
        return True

    def process(self):
        # guidance = self.network.text_guidance(self.device.position)
        guidance = "bel"
        if self.last_guidance != guidance:
            return os.system("tput bel") if guidance == "bel" else\
                os.system("say -v Thomas \"{}\" &".format(guidance))

    def close(self):
        self.last_guidance = None
        lc.log.debug("Closing Voice interaction")


class KeyboardInteract(DefaultInteract):
    def __init__(self):
        super().__init__()

    def open(self):
        super().open()
        self.last_guidance = None
        try:
            os.system("say -v Thomas \"Initialization\" &")
        except Exception as e:
            lc.log.warning("Cannot use 'say' command, (not on OSX?): ", e)
            return False
        return True

    def process(self):
        pass

    def close(self):
        pass
