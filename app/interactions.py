import serial
import time
import os

import app.logconfig as lc
# from app.network import Node, Link
from app.behavior import Behavior, State


class DefaultInteract(object):
    SIMULATION = True

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
    # SERIAL_PATH = '/dev/cu.usbmodem1411'
    SERIAL_PATH = '/dev/cu.DrAdrien-DevB'

    def __init__(self):
        super().__init__()
        self.to_apply = {}

    def open(self):
        super().open()
        self.to_apply = {
            act: [Behavior([0])] for act in self.device.actuators}
        if DefaultInteract.SIMULATION:
            return True
        lc.log.debug("Trying opening serial")
        try:
            self.ser = serial.Serial(
                HaptiQInteract.SERIAL_PATH, baudrate=115200, timeout=0)
            lc.log.info("Serial openned")
        except:
            lc.log.warning("Cannot open serial communication.")
            return False
        return True

    def apply(self,):
        for act in self.device.actuators:
            if act in self.to_apply:
                n_level = sum([b.next() for b in self.to_apply[act]])
                if n_level != act.level:
                    act.level = n_level
                    msg = 's{}{}f'.format(
                        str(self.device.actuators.index(act)),
                        str(act.level).zfill(2)
                    )
                    lc.log.debug("serial sending: " + msg)
                    if not DefaultInteract.SIMULATION:
                        self.ser.write(bytes(msg, 'UTF-8'))
        Behavior._iter += 1
        lc.log.info('actuators: ' + ', '.join(
            [str(act) for act in self.device.actuators]))
        time.sleep(0.2)

    def close(self):
        if DefaultInteract.SIMULATION:
            return True
        self.ser.close()
        lc.log.info("Serial closed")


class OscillateMapping(HaptiQInteract):
    def __init__(self):
        super().__init__()

    def process(self):
        self.to_apply = {act: [Behavior([0])] for act in self.device.actuators}
        pos = self.device.position
        node_under = next((nd for nd in self.view.network.nodes if State.which(
            nd.distance_to(pos)) == State.on), None)
        lnks_under = [lk for lk in self.view.network.links if State.which(
            lk.distance_to(pos)) == State.on]
        if node_under:
            for lk in lnks_under:
                for act in self.device.actuators_for(lk):
                    self.to_apply[act].append(Behavior([99]))
        else:
            cl = None  # closest link
            for lk in lnks_under:
                if lk.closer_than(cl, pos):
                    cl = lk
            for act in self.device.actuators_for(cl):
                self.to_apply[act].append(
                    Behavior(Behavior.gen_oscillation(0, 90, 10)))
        super().apply()


class OscillateGuidance(HaptiQInteract):
    def __init__(self):
        super().__init__()

    def process(self):
        self.to_apply = {act: [Behavior([0])] for act in self.device.actuators}
        pos = self.device.position
        node_under = next((nd for nd in self.view.network.nodes if State.which(
            nd.distance_to(pos)) == State.on), None)
        if node_under:
            for lk in self.view.network.links:
                if State.which(lk.distance_to(pos)) == State.on:
                    [act] = self.device.actuators_for(lk)
                    self.to_apply[act].append(Behavior([99]))
        elif len(self.view.network.links) > 0:
            cl = None  # closest link
            for lk in self.view.network.links:
                if lk.closer_than(cl, pos):
                    cl = lk
            if State.which(cl.distance_to(pos)) == State.on:
                for act in self.device.actuators_for(cl):
                    self.to_apply[act].append(
                        Behavior(Behavior.gen_oscillation(0, 90, 10)))
            elif State.which(cl.distance_to(pos)) == State.hot:
                self.to_apply[self.device.actuator_to(cl)].append(
                    Behavior(Behavior.gen_oscillation(0, 20, 10)))
            else:
                self.to_apply[self.device.actuator_to(cl)].append(
                    Behavior([20]))
        super().apply()


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
