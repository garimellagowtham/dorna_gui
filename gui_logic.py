#!/usr/bin/env python
import robot_utils as utils
import json
from slot_manager import SlotManager
from logger import Logger
from position_command_layout import Ui_position_command_layout
from servo_layout import Ui_servo_layout
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog
from PyQt5.QtCore import QTimer, Qt
from types import SimpleNamespace
import vegetable_cutting_utils as cutting_utils


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


def fillGoalPosition(relative_state, dialog_layout, robot):
    if relative_state != Qt.Checked:
        # Fill default values
        xyzab = json.loads(robot.position('xyzab'))
        xyzab = [0.0 if val is None else val for val in xyzab]
    else:
        xyzab = [0.0]*5
    dialog_layout.goal_x.setText('{0:.2f}'.format(xyzab[0]))
    dialog_layout.goal_y.setText('{0:.2f}'.format(xyzab[1]))
    dialog_layout.goal_z.setText('{0:.2f}'.format(xyzab[2]))
    dialog_layout.goal_a.setText('{0:.2f}'.format(xyzab[3]))
    dialog_layout.goal_b.setText('{0:.2f}'.format(xyzab[4]))


def create_position_dialog(robot):
    goal_position_dialog = QDialog()
    dialog_layout = Ui_position_command_layout()
    dialog_layout.setupUi(goal_position_dialog)
    dialog_layout.relative.stateChanged.connect(lambda x: fillGoalPosition(
        x, dialog_layout, robot))
    fillGoalPosition(Qt.Unchecked, dialog_layout, robot)
    button_input = goal_position_dialog.exec_()
    if button_input == QDialog.Accepted:
        result = SimpleNamespace()
        result.xyzab = [float(dialog_layout.goal_x.text()),
                        float(dialog_layout.goal_y.text()),
                        float(dialog_layout.goal_z.text()),
                        float(dialog_layout.goal_a.text()),
                        float(dialog_layout.goal_b.text())]
        result.movement = 1 if dialog_layout.relative.checkState() == Qt.Checked else 0
        dialog_speed = float(dialog_layout.goal_speed.text())
        result.speed = None if dialog_speed == 0 else dialog_speed
        return result
    else:
        return None

def create_servo_dialog(robot):
    servo_dialog =QDialog()
    servo_layout = Ui_servo_layout()
    servo_layout.setupUi(servo_dialog)
    if robot.servo_position > 0:
        servo_layout.servo_slider.setSliderPosition(robot.servo_position)
    button_input = servo_dialog.exec_()
    if button_input== QDialog.Accepted:
        return servo_layout.servo_slider.sliderPosition()
    return None

class GUILogic(object):
    def __init__(self, gui_layout, gui_window, dorna_robot):
        self.gui_layout = gui_layout
        self.gui_window = gui_window
        self.robot = dorna_robot
        # Adding servo location to robot for easy access
        self.robot.servo_position = -1
        self.robot_connected = False
        self.robot_stopped = False
        self.status_timer = QTimer(self.gui_window)
        Logger.initialize(self.gui_layout.log_box)
        SlotManager.set_update_robot_status_fn(self.reset_stop_flag)
        SlotManager.set_status_check_fn(self.status_check)
        # Create a slot manager that performs a single cut
        self.vegetable_cut_slot_manager = SlotManager(
            self.vegetable_cut_action_processing,
            exit_fcn=self.vegetable_cut_action_process_exit)
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
        gui_layout.position_action.clicked.connect(SlotManager(
            self.position_action_clicked,
            initialize_fcn=lambda: create_position_dialog(self.robot)))
        gui_layout.servo_action.clicked.connect(SlotManager(
            self.servo_action_clicked,
            initialize_fcn=lambda: create_servo_dialog(self.robot)))
        gui_layout.vegetable_cut_action.clicked.connect(SlotManager(
            self.vegetable_cut_action_positioning,
            initialize_fcn=cutting_utils.create_vegetable_cutting_dialog,
            exit_fcn=self.vegetable_cut_action_process_exit))
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
        # Set angles
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
            Logger.log("Failed to connect to port")
        else:
            show_message(("Successfully connected to robot!"
                          " Please calibrate if u recently "
                          "power cycled the arm"),
                         message_type=QMessageBox.Information,
                         get_response=False)
            Logger.log("Connected!")
            Logger.log("Please calibrate if not already calibrated!")
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

    def position_action_clicked(self, _, user_input):
        if user_input is not None:
            Logger.log("Sending position command: ", user_input)
            utils.move(self.robot, user_input.xyzab,
                       movement=user_input.movement, speed=user_input.speed)
        else:
            Logger.log("User cancelled input")

    def vegetable_cut_action_positioning(self, _, user_input):
        if user_input is not None:
            Logger.log("Positioning to cut: ", user_input.origin)
            z_offset = 11.0 - user_input.origin[2]
            assert z_offset > 0
            utils.hopThroughWaypoint(self.robot, user_input.origin, z_offset,
                                     user_input.cut_speed)
        else:
            Logger.log("User cancelled input")

    def vegetable_cut_action_processing(self, _, user_input):
        if user_input is not None:
            Logger.log("Performing a single cut")
            cutting_utils.perform_single_cut_action(
                self.robot, self.status_check, user_input)
        else:
            Logger.log("User cancelled input")

    def vegetable_cut_action_process_exit(self, button_status, user_input):
        user_proceed = show_message(
            "Ready to cut?", message_type=QMessageBox.Warning)
        if user_proceed == QMessageBox.Ok:
            self.vegetable_cut_slot_manager(button_status, user_input)
        else:
            Logger.log("Finished Cutting!")

    def home_action_clicked(self, _):
        Logger.log("GuiManager: Going home")
        result = utils.goHome(self.robot, j3=-19, j4=70)
        utils.blockUntilComplete(self.robot, result)

    def servo_action_clicked(self, _, user_input):
        if user_input is not None:
            Logger.log("GuiManager: Setting servo: {}".format(user_input))
            self.robot.servo(float(user_input))
            self.robot.servo_position = user_input


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
