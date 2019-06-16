#!/usr/bin/env python
from PyQt5.QtWidgets import QDialog
from types import SimpleNamespace
from vegetable_cut_layout import Ui_VegetableCutLayout
import robot_utils as utils
from logger import Logger

# Cutting params (No need to adjust unless you understand them)
cut_horizontal_angle = -116
tolerance_vegetable_height = 0.2
vegetable_x = 12.8
cut_y_start = -2.0  # Start y value
min_z_height = 2.66
cut_direction = 1  # Along positive y is +1


def fill_default_values(dialog_layout):
    # User params
    slice_width = 0.5
    vegetable_height = 0.8  # The height of vegetable to cut
    vegetable_width = 4.5  # The width of vegetable to cut
    stroke_length = 0.5
    cut_speed = 100
    # Fill values
    start_height = vegetable_height + tolerance_vegetable_height + min_z_height
    xyzab = [vegetable_x, 0, start_height, -100, 70]
    dialog_layout.origin_x.setText('{0:.2f}'.format(xyzab[0]))
    dialog_layout.origin_y.setText('{0:.2f}'.format(xyzab[1]))
    dialog_layout.origin_z.setText('{0:.2f}'.format(xyzab[2]))
    dialog_layout.origin_a.setText('{0:.2f}'.format(xyzab[3]))
    dialog_layout.origin_b.setText('{0:.2f}'.format(xyzab[4]))
    dialog_layout.vegetable_height.setText('{0:.2f}'.format(vegetable_height))
    dialog_layout.vegetable_width.setText('{0:.2f}'.format(vegetable_width))
    dialog_layout.slice_width.setText('{0:.2f}'.format(slice_width))
    dialog_layout.stroke_length.setText('{0:.2f}'.format(stroke_length))
    dialog_layout.cut_speed.setText('{0:.1f}'.format(cut_speed))


def create_vegetable_cutting_dialog():
    goal_position_dialog = QDialog()
    dialog_layout = Ui_VegetableCutLayout()
    dialog_layout.setupUi(goal_position_dialog)
    fill_default_values(dialog_layout)
    button_input = goal_position_dialog.exec_()
    if button_input == QDialog.Accepted:
        result = SimpleNamespace()
        result.origin = [float(dialog_layout.origin_x.text()),
                         float(dialog_layout.origin_y.text()),
                         float(dialog_layout.origin_z.text()),
                         float(dialog_layout.origin_a.text()),
                         float(dialog_layout.origin_b.text())]
        result.vegetable_height = float(dialog_layout.vegetable_height.text())
        result.vegetable_width = float(dialog_layout.vegetable_width.text())
        result.slice_width = float(dialog_layout.slice_width.text())
        result.stroke_length = float(dialog_layout.stroke_length.text())
        result.cut_speed = float(dialog_layout.cut_speed.text())
        return result
    else:
        return None


def cut(robot, cut_properties, status_check_fun):
    n_strokes = int(cut_properties.vegetable_width//cut_properties.slice_width)
    for stroke in range(n_strokes):
        if not status_check_fun():
            Logger.log("Cutting: Status check failed!")
            return
        # Downstroke
        utils.move(robot, {'x': cut_properties.stroke_length, 'z': -cut_properties.cutting_height},
                   movement=1, speed=cut_properties.cut_speed)
        # Upstroke
        utils.move(robot, {'x': -cut_properties.stroke_length, 'z': cut_properties.cutting_height},
                   movement=1, speed=cut_properties.cut_speed)
        # Move to right y offset
        res = utils.move(robot, {'y': cut_direction*cut_properties.slice_width, 'b': 2.0}, movement=1,
                         speed=cut_properties.cut_speed)
        utils.blockUntilComplete(robot, res)


def sweep(robot, cut_properties, status_check_fn):
    Logger.log("Sweeping")
    if not status_check_fn():
        Logger.log("Cutting: Status check failed!")
        return
    utils.move(robot, {'y': -1.2*cut_direction*cut_properties.vegetable_width}, movement=1,
               speed=cut_properties.cut_speed)
    utils.move(robot, {'z': -cut_properties.cutting_height+0.08}, movement=1,
               speed=cut_properties.cut_speed)
    utils.move(robot, {'y': 1.2*cut_direction *
                       cut_properties.vegetable_width}, movement=1)
    utils.move(robot, {'z': cut_properties.cutting_height+0.1}, movement=1)
    res = utils.move(robot, {'y': -1.2*cut_direction*cut_properties.vegetable_width},
                     movement=1, speed=cut_properties.cut_speed)
    utils.blockUntilComplete(robot, res)


def perform_single_cut_action(robot, status_check_fn, cut_properties):
    if not status_check_fn():
        Logger.log("Cutting: Status check failed!")
        return
    start_height = cut_properties.origin[2]
    cut_properties.cutting_height = (start_height - min_z_height)
    cut_start = list(cut_properties.origin)
    cut_start[1] = cut_y_start
    cut_start[3] = cut_horizontal_angle
    Logger.log("Positioning to cut: ", cut_start)
    res = utils.move(robot, cut_start,
                     speed=cut_properties.cut_speed, movement=0)
    utils.blockUntilComplete(robot, res)
    Logger.log("Cutting!")
    cut(robot, cut_properties, status_check_fn)
    Logger.log("Sweeping")
    sweep(robot, cut_properties, status_check_fn)
