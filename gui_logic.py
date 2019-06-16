#!/usr/bin/env python
import robot_utils as utils
import json
from slot_manager import SlotManager
from logger import Logger
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer


def show_message(short_message, detailed_message="",
                 message_type=QMessageBox.Information, get_response=True):
    msg_box = QMessageBox()
    msg_box.setIcon(message_type)
    msg_box.setText(short_message)
    if len(detailed_message) != 0:
        msg_box.setInformativeText(detailed_message)
    if get_response:
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg_box.exec_()


class GUILogic(object):
    def __init__(self, gui_layout, gui_window, dorna_robot):
        self.gui_layout = gui_layout
        self.gui_window = gui_window
        self.robot = dorna_robot
        self.robot_connected = False
        self.robot_stopped = False
        self.status_timer = QTimer(self.gui_window)
        Logger.initialize(self.gui_layout.log_box)
        SlotManager.set_update_robot_status_fn(self.reset_stop_flag)
        # Connect all signals and slots
        gui_layout.stop_action.clicked.connect(self.stop_action_clicked)
        gui_layout.home_action.clicked.connect(SlotManager(
            self.home_action_clicked))
        gui_layout.calibrate_action.clicked.connect(SlotManager(
            self.calibrate_action_clicked,
            initialize_fcn=lambda: show_message(
                short_message=("Are you ready to calibrate!! Make sure"
                               " there is nothing around the robot!!"),
                message_type=QMessageBox.Warning)))
        gui_layout.gcode_action.clicked.connect(SlotManager(
            self.gcode_action_clicked,
            initialize_fcn=lambda: QFileDialog.getOpenFileName(
                caption="Choose CNC File",
                filter="Cnc Files(*.cnc *.txt)")))
        gui_layout.connect_arm.clicked.connect(self.connect_arm_clicked)
        self.status_timer.timeout.connect(self.update_status)
        # Start timers
        self.status_timer.start(500)

    def status_check(self):
        return self.robot_connected and not self.robot_stopped

    def reset_stop_flag(self):
        self.robot_stopped = False

    def update_status(self):
        if self.robot_connected is False:
            return
        device_info = json.loads(self.robot.device())
        self.robot_connected = False
        connection = device_info["connection"]
        if connection == 2:
            self.robot_connected = True
            self.gui_layout.connection_status_label.setText('Connected')
        elif connection == 1:
            self.gui_layout.connection_status_label.setText('Connecting')
        elif connection == 0:
            self.gui_layout.connection_status_label.setText('Disconnected')
        else:
            self.gui_layout.connection_status_label.setText(
                'Unknown: {}'.format(connection))
        robot_state = device_info["state"]
        if robot_state == 0:
            self.gui_layout.robot_status_label.setText('Ready')
        elif robot_state == 1:
            self.gui_layout.robot_status_label.setText('Busy')
        else:
            self.gui_layout.robot_status_label.setText(
                'Unknown: {}'.format(robot_state))
        # Set position state
        xyzab = json.loads(self.robot.position('xyzab'))
        xyzab = [0.0 if val is None else val for val in xyzab]
        self.gui_layout.state_x.setText('{0:.4f}'.format(xyzab[0]))
        self.gui_layout.state_y.setText('{0:.4f}'.format(xyzab[1]))
        self.gui_layout.state_z.setText('{0:.4f}'.format(xyzab[2]))
        self.gui_layout.state_a.setText('{0:.4f}'.format(xyzab[3]))
        self.gui_layout.state_b.setText('{0:.4f}'.format(xyzab[4]))
        angles = json.loads(self.robot.position('joint'))
        angles = [0.0 if val is None else val for val in angles]
        self.gui_layout.state_j0.setText('{0:.2f}'.format(angles[0]))
        self.gui_layout.state_j1.setText('{0:.2f}'.format(angles[1]))
        self.gui_layout.state_j2.setText('{0:.2f}'.format(angles[2]))
        self.gui_layout.state_j3.setText('{0:.2f}'.format(angles[3]))
        self.gui_layout.state_j4.setText('{0:.2f}'.format(angles[4]))

    # Slots for UI Buttons
    def connect_arm_clicked(self, _):
        user_input = self.gui_layout.arm_port.text()
        port_name = None if user_input == "" else user_input
        Logger.log("Opening port: ", port_name)
        json_status = self.robot.connect(port_name=port_name)
        status = json.loads(json_status)
        if status["connection"] != 2:
            self.robot_connected = False
            show_message("Cannot connect to robot: {}".format(json_status),
                         message_type=QMessageBox.Warning,
                         get_response=False)
        else:
            self.robot_connected = True

    def stop_action_clicked(self, _):
        self.robot_stopped = True
        self.robot.halt()

    def calibrate_action_clicked(self, _, user_input):
        if user_input == QMessageBox.Ok:
            Logger.log("GuiManager: Calibrating robot!")
            utils.calibrate(self.robot, self.status_check)
        else:
            Logger.log("Cancelling command")

    def home_action_clicked(self, _):
        if self.status_check():
            Logger.log("GuiManager: Going home")
            result = utils.goHome(self.robot, j3=-19, j4=70)
            utils.blockUntilComplete(self.robot, result)
        else:
            Logger.log("GuiManager: Status check failed")

    def gcode_action_clicked(self, _, user_input):
        if len(user_input) == 2 and len(user_input[0]) != 0:
            cnc_file = user_input[0]
            origin_for_drawing = [13, 2, 0.89, -16, -35]
            Logger.log('Loading Cnc file: ', cnc_file)
            utils.drawCnc(self.robot, cnc_file, origin_for_drawing,
                          self.status_check)
        else:
            Logger.log("GuiManager: Cancelled cnc drawing since user"
                       " did not select a file")
