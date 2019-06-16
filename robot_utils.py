#!/usr/bin/env python3
import time
import json
from logger import Logger

"""
Utility functions for dorna robot
"""


def calibrate(robot, status_check_fn):
    for j in range(4):
        joint = 'j'+str(j)
        if status_check_fn():
            Logger.log("Dorna: Homing "+joint)
            robot.home(joint)
        else:
            Logger.log("Dorna: Aborting due to status failed")
            break


def blockUntilComplete(robot, result, wait_time=15.0):
    result = json.loads(result)
    if len(result) != 0:
        robot._wait_for_command(result, time.time()+wait_time)


def move(robot, xyzab, movement=0, speed=None):
    input_dict = {"movement": movement, "path": "line"}
    if type(xyzab) == dict:
        for key in xyzab:
            input_dict[key] = xyzab[key]
    else:
        keys = ['x', 'y', 'z', 'a', 'b']
        for i, val in enumerate(xyzab):
            input_dict[keys[i]] = val
    if speed is not None:
        input_dict['speed'] = speed
    return robot.move(input_dict)


def hopThroughWaypoint(robot, goal, z_offset=12, speed=100):
    waypoint = goal.copy()
    waypoint[2] = waypoint[2] + z_offset
    move(robot, waypoint, speed=speed)
    move(robot, [0, 0, -z_offset, 0, 0], movement=1, speed=speed)


def goHome(robot, j3=0, j4=20):
    res = robot.move({"movement": 0, "path": "joint",
                      "j0": 0, "j1": 145, "j2": -90, 'j3': j3, 'j4': j4})
    return res


def _translate_coordinates(coordinates):
    command = {}
    for coordinate in coordinates:
        key = coordinate[0]
        val = coordinate[1:]
        mapping_key = {'x': 'y', 'y': 'x', 'i': 'j', 'j': 'i'}
        if key in ['X', 'I']:
            command[mapping_key[key.lower()]] = -float(val)
        elif key in ['Y', 'J']:
            command[mapping_key[key.lower()]] = float(val)
        elif key in ['Z', 'K']:
            command[key.lower()] = float(val)
        elif key == 'P':
            command[key.lower()] = int(val)
    return command


def drawCnc(robot, cnc_file, origin_for_drawing, status_check_fn):
    origin = {'x': origin_for_drawing[0], 'y': origin_for_drawing[1],
              'z': origin_for_drawing[2], 'a': origin_for_drawing[3],
              'b': origin_for_drawing[4]}
    with open(cnc_file, 'r') as f:
        for line in f.readlines():
            if not status_check_fn():
                Logger.log("Status failed")
                return
            if len(line) == 0 or line[0] == '(':
                continue
            words = line.split(' ')
            # assertlength
            command = _translate_coordinates(words[2:])
            if words[1] == 'G0' or words[1] == 'G1':
                for key in command:
                    command[key] = command[key] + origin[key]
                result = move(robot, command)
                blockUntilComplete(robot, result, 0.1)
            elif words[1] == 'G2' or words[1] == 'G3':
                circle_command = {'M': 0, 'movement': 0, }
                for key in command:
                    if key in ['x', 'y', 'z']:
                        circle_command[key.upper()] = command[key] + \
                            origin[key]
                    else:
                        circle_command[key.upper()] = command[key]
                result = robot.move_circle(circle_command)
                blockUntilComplete(robot, result, 0.1)
            else:
                print("Unknown command ignoring ...")
    # A little higher (by 1 in) after drawing the cnc
    result = move(robot, [0, 0, 1, 0, 0], 1)
    blockUntilComplete(robot, result, 0.1)
