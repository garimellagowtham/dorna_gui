#!/usr/bin/env python


class DornaManager(object):
    def __init__(self, robot):
        self.robot = robot

    def __enter__(self):
        pass

    def __exit__(self, t, value, traceback):
        print("Terminating robot")
        self.robot.terminate()
