import serial
import time
import os

import app.logconfig as lc
from app.network import Node, Link
from app.behavior import Behavior, State


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
        self.to_apply = {}

    def open(self):
        super().open()
        self.to_apply = {act: [Behavior([0])] for act in self.device.actuators}
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

    def process(self):
        self.to_apply = {act: [Behavior([0])] for act in self.device.actuators}
        # Fetch infos
        context = self.view.network.distances(self.device.position)
        under = {
            elem: context[elem] for elem in context if (
                State.which(context[elem]['distance']) == State.on)
        }
        # Build behaviors
        for elem in under:
            if type(elem) == Node:
                for act in self.to_apply:
                    self.to_apply[act].append(Behavior([45]))
            elif type(elem) == Link:
                for act in self.device.actuators_for(elem):
                    self.to_apply[act].append(Behavior([45]))
        # Apply
        for act in self.device.actuators:
            if act in self.to_apply:
                n_level = sum([b.next() for b in self.to_apply[act]])
                if n_level != act.level:
                    act.level = n_level
                    msg = 's{}{}f'.format(
                        str(self.device.actuators.index(act)), str(act.level))
                    lc.log.debug("serial sending: " + msg)
                    if not DefaultInteract.SIMULATION:
                        self.ser.write(bytes(msg, 'UTF-8'))
        Behavior._iter += 1
        time.sleep(0.1)

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
