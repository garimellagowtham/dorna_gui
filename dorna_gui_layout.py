# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dorna_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dorna_main_gui(object):
    def setupUi(self, dorna_main_gui):
        dorna_main_gui.setObjectName("dorna_main_gui")
        dorna_main_gui.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(dorna_main_gui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image_scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.image_scroll_area.setAutoFillBackground(True)
        self.image_scroll_area.setWidgetResizable(True)
        self.image_scroll_area.setObjectName("image_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 260))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.image_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image_label.setGeometry(QtCore.QRect(0, 10, 331, 251))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setText("")
        self.image_label.setScaledContents(True)
        self.image_label.setObjectName("image_label")
        self.image_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.image_scroll_area, 1, 0, 1, 1)
        self.arm_connection = QtWidgets.QHBoxLayout()
        self.arm_connection.setObjectName("arm_connection")
        self.arm_port_label = QtWidgets.QLabel(self.centralwidget)
        self.arm_port_label.setObjectName("arm_port_label")
        self.arm_connection.addWidget(self.arm_port_label)
        self.arm_port = QtWidgets.QLineEdit(self.centralwidget)
        self.arm_port.setObjectName("arm_port")
        self.arm_connection.addWidget(self.arm_port)
        self.connect_arm = QtWidgets.QPushButton(self.centralwidget)
        self.connect_arm.setObjectName("connect_arm")
        self.arm_connection.addWidget(self.connect_arm)
        self.gridLayout.addLayout(self.arm_connection, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.status_label.setObjectName("status_label")
        self.horizontalLayout.addWidget(self.status_label)
        self.connection_status_label = QtWidgets.QLabel(self.centralwidget)
        self.connection_status_label.setObjectName("connection_status_label")
        self.horizontalLayout.addWidget(self.connection_status_label)
        self.robot_status_label = QtWidgets.QLabel(self.centralwidget)
        self.robot_status_label.setObjectName("robot_status_label")
        self.horizontalLayout.addWidget(self.robot_status_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.arm_status_grid = QtWidgets.QGridLayout()
        self.arm_status_grid.setObjectName("arm_status_grid")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.arm_status_grid.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.arm_status_grid.addWidget(self.label_4, 0, 0, 1, 1)
        self.state_z = QtWidgets.QLabel(self.centralwidget)
        self.state_z.setObjectName("state_z")
        self.arm_status_grid.addWidget(self.state_z, 0, 3, 1, 1)
        self.state_j2 = QtWidgets.QLabel(self.centralwidget)
        self.state_j2.setObjectName("state_j2")
        self.arm_status_grid.addWidget(self.state_j2, 1, 3, 1, 1)
        self.state_j1 = QtWidgets.QLabel(self.centralwidget)
        self.state_j1.setObjectName("state_j1")
        self.arm_status_grid.addWidget(self.state_j1, 1, 2, 1, 1)
        self.state_j4 = QtWidgets.QLabel(self.centralwidget)
        self.state_j4.setObjectName("state_j4")
        self.arm_status_grid.addWidget(self.state_j4, 1, 5, 1, 1)
        self.state_b = QtWidgets.QLabel(self.centralwidget)
        self.state_b.setObjectName("state_b")
        self.arm_status_grid.addWidget(self.state_b, 0, 5, 1, 1)
        self.state_y = QtWidgets.QLabel(self.centralwidget)
        self.state_y.setObjectName("state_y")
        self.arm_status_grid.addWidget(self.state_y, 0, 2, 1, 1)
        self.state_x = QtWidgets.QLabel(self.centralwidget)
        self.state_x.setObjectName("state_x")
        self.arm_status_grid.addWidget(self.state_x, 0, 1, 1, 1)
        self.state_j0 = QtWidgets.QLabel(self.centralwidget)
        self.state_j0.setObjectName("state_j0")
        self.arm_status_grid.addWidget(self.state_j0, 1, 1, 1, 1)
        self.state_j3 = QtWidgets.QLabel(self.centralwidget)
        self.state_j3.setObjectName("state_j3")
        self.arm_status_grid.addWidget(self.state_j3, 1, 4, 1, 1)
        self.state_a = QtWidgets.QLabel(self.centralwidget)
        self.state_a.setObjectName("state_a")
        self.arm_status_grid.addWidget(self.state_a, 0, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.arm_status_grid)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.arm_log = QtWidgets.QVBoxLayout()
        self.arm_log.setObjectName("arm_log")
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setObjectName("log_label")
        self.arm_log.addWidget(self.log_label)
        self.log_box = QtWidgets.QTextEdit(self.centralwidget)
        self.log_box.setReadOnly(True)
        self.log_box.setObjectName("log_box")
        self.arm_log.addWidget(self.log_box)
        self.gridLayout.addLayout(self.arm_log, 2, 0, 1, 1)
        self.action_grid = QtWidgets.QGridLayout()
        self.action_grid.setContentsMargins(6, -1, -1, -1)
        self.action_grid.setHorizontalSpacing(20)
        self.action_grid.setVerticalSpacing(6)
        self.action_grid.setObjectName("action_grid")
        self.vegetable_cut_action = QtWidgets.QPushButton(self.centralwidget)
        self.vegetable_cut_action.setObjectName("vegetable_cut_action")
        self.action_grid.addWidget(self.vegetable_cut_action, 2, 0, 1, 1)
        self.action_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.action_label.setFont(font)
        self.action_label.setAlignment(QtCore.Qt.AlignCenter)
        self.action_label.setObjectName("action_label")
        self.action_grid.addWidget(self.action_label, 0, 0, 1, 1)
        self.calibrate_action = QtWidgets.QPushButton(self.centralwidget)
        self.calibrate_action.setObjectName("calibrate_action")
        self.action_grid.addWidget(self.calibrate_action, 2, 1, 1, 1)
        self.home_action = QtWidgets.QPushButton(self.centralwidget)
        self.home_action.setObjectName("home_action")
        self.action_grid.addWidget(self.home_action, 0, 3, 1, 1)
        self.gcode_action = QtWidgets.QPushButton(self.centralwidget)
        self.gcode_action.setObjectName("gcode_action")
        self.action_grid.addWidget(self.gcode_action, 2, 2, 1, 1)
        self.position_action = QtWidgets.QPushButton(self.centralwidget)
        self.position_action.setObjectName("position_action")
        self.action_grid.addWidget(self.position_action, 2, 3, 1, 1)
        self.stop_action = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stop_action.sizePolicy().hasHeightForWidth())
        self.stop_action.setSizePolicy(sizePolicy)
        self.stop_action.setMaximumSize(QtCore.QSize(160, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.stop_action.setFont(font)
        self.stop_action.setObjectName("stop_action")
        self.action_grid.addWidget(self.stop_action, 0, 1, 1, 2)
        self.gridLayout.addLayout(self.action_grid, 2, 1, 1, 1)
        self.image_text_label = QtWidgets.QLabel(self.centralwidget)
        self.image_text_label.setObjectName("image_text_label")
        self.gridLayout.addWidget(self.image_text_label, 0, 0, 1, 1)
        dorna_main_gui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(dorna_main_gui)
        self.statusbar.setObjectName("statusbar")
        dorna_main_gui.setStatusBar(self.statusbar)

        self.retranslateUi(dorna_main_gui)
        QtCore.QMetaObject.connectSlotsByName(dorna_main_gui)

    def retranslateUi(self, dorna_main_gui):
        _translate = QtCore.QCoreApplication.translate
        dorna_main_gui.setWindowTitle(
            _translate("dorna_main_gui", "MainWindow"))
        self.arm_port_label.setText(_translate("dorna_main_gui", "Arm Port"))
        self.arm_port.setText(_translate("dorna_main_gui", "/dev/ttyACM0"))
        self.connect_arm.setText(_translate("dorna_main_gui", "Connect"))
        self.status_label.setText(_translate("dorna_main_gui", "Status"))
        self.connection_status_label.setText(
            _translate("dorna_main_gui", "Disconnected"))
        self.robot_status_label.setText(_translate("dorna_main_gui", "Ready"))
        self.label_5.setText(_translate("dorna_main_gui", "Joints"))
        self.label_4.setText(_translate("dorna_main_gui", "Position"))
        self.state_z.setText(_translate("dorna_main_gui", "0"))
        self.state_j2.setText(_translate("dorna_main_gui", "0"))
        self.state_j1.setText(_translate("dorna_main_gui", "0"))
        self.state_j4.setText(_translate("dorna_main_gui", "0"))
        self.state_b.setText(_translate("dorna_main_gui", "0"))
        self.state_y.setText(_translate("dorna_main_gui", "0"))
        self.state_x.setText(_translate("dorna_main_gui", "0"))
        self.state_j0.setText(_translate("dorna_main_gui", "0"))
        self.state_j3.setText(_translate("dorna_main_gui", "0"))
        self.state_a.setText(_translate("dorna_main_gui", "0"))
        self.log_label.setText(_translate("dorna_main_gui", "Log"))
        self.vegetable_cut_action.setText(
            _translate("dorna_main_gui", "Vegetable"))
        self.action_label.setText(_translate("dorna_main_gui", "Commands"))
        self.calibrate_action.setText(
            _translate("dorna_main_gui", "Calibrate"))
        self.home_action.setText(_translate("dorna_main_gui", "GoHome"))
        self.gcode_action.setText(_translate("dorna_main_gui", "Gcode"))
        self.position_action.setText(_translate("dorna_main_gui", "Position"))
        self.stop_action.setText(_translate("dorna_main_gui", "STOP"))
        self.image_text_label.setText(_translate("dorna_main_gui", "Image"))