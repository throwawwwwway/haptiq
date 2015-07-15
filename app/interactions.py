import serial
import time
import os

import app.logconfig as lc
# from app.network import Node, Link
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
        self.to_apply = {
            act: [Behavior([0])] for act in self.device.actuators}
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
        time.sleep(0.1)

    def close(self):
        if DefaultInteract.SIMULATION:
            return True
        self.ser.close()
        lc.log.debug("Closing HaptiQ interaction")


class StableMapping(HaptiQInteract):
    def __init__(self):
        super().__init__()

    def process(self):
        self.to_apply = {
            act: [Behavior([0])] for act in self.device.actuators}
        # Fetch infos & build behaviors
        for node in self.view.network.nodes:
            if State.which(node.distance_to(self.device.position)) == State.on:
                for act in self.device.actuators:
                    self.to_apply[act].append(Behavior([45]))
                break
        for link in self.view.network.links:
            if State.which(link.distance_to(self.device.position)) == State.on:
                for act in self.device.actuators_for(link):
                    self.to_apply[act].append(Behavior([45]))
        super().apply()


class OscillateMapping(HaptiQInteract):
    def __init__(self):
        super().__init__()

    def process(self):
        self.to_apply = {act: [Behavior()] for act in self.device.actuators}
        behavior = Behavior(
            list(range(0, 90, 10)) + list(range(10, 91, 10))[::-1])
        for node in self.view.network.nodes:
            if State.which(node.distance_to(self.device.position)) == State.on:
                behavior = Behavior([99])
                break
        for link in self.view.network.links:
            if State.which(link.distance_to(self.device.position)) == State.on:
                for act in self.device.actuators_for(link):
                    self.to_apply[act].append(behavior)
        super().apply()


class SimpleGuidance(HaptiQInteract):
    def __init__(self):
        super().__init__()

    def process(self):
        self.to_apply = {act: [Behavior()] for act in self.device.actuators}
        prox_nd = None
        for node in self.view.network.nodes:
            if State.which(node.distance_to(self.device.position)) == State.on:
                for act in self.device.actuators:
                    self.to_apply[act].append(Behavior([44]))
                prox_nd = None
                break
            elif node.closer_than(prox_nd, self.device.position):
                prox_nd = node
        if prox_nd is not None:
            state = State.which(prox_nd.distance_to(self.device.position))
            if state == State.cold:
                seq = Behavior.gen_oscillation(0, 40, 5)
            elif state == State.hot:
                seq = Behavior.gen_oscillation(0, 40, 20)
            else:
                seq = [0]
            self.to_apply[self.device.actuator_to(prox_nd)].append(
                Behavior(seq))
        for link in self.view.network.links:
            if State.which(link.distance_to(self.device.position)) == State.on:
                for act in self.device.actuators_for(link):
                    self.to_apply[act].append(Behavior([44]))
        super().apply()


class ComplexGuidance(HaptiQInteract):
    def __init__(self):
        super().__init__()

    def process(self):
        pass


# class OscillateMapping(HaptiQInteract):
#     def __init__(self):
#         super().__init__()

#     def process(self):
#        self.to_apply = {act: [Behavior([0])] for act in self.device.actuators
#         context = self.view.network.distances(self.device.position)
#         acts = []
#         on_node = False
#         for elem in context:
#             if (type(elem) == Node and
#                     State.which(context[elem]['distance']) == State.on):
#                 on_node = True
#             elif :

#             if type(elem) == Link
#         s_elems = sorted(
#             context, key=lambda e: (group(e), context[e]['distance']))

#         else:


#         context = self.view.network.distances(self.device.position)
#         node = [elem for elem in context if (type(elem) == Node and
#                 State.which(context[elem]['distance']) == State.on)]


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
