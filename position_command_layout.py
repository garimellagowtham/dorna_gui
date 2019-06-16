# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './position_command_layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_position_command_layout(object):
    def setupUi(self, position_command_layout):
        position_command_layout.setObjectName("position_command_layout")
        position_command_layout.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(position_command_layout)
        self.formLayout.setObjectName("formLayout")
        self.goal_x = QtWidgets.QLineEdit(position_command_layout)
        self.goal_x.setObjectName("goal_x")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.goal_x)
        self.goal_y = QtWidgets.QLineEdit(position_command_layout)
        self.goal_y.setObjectName("goal_y")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.goal_y)
        self.goal_z = QtWidgets.QLineEdit(position_command_layout)
        self.goal_z.setObjectName("goal_z")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.goal_z)
        self.goal_a = QtWidgets.QLineEdit(position_command_layout)
        self.goal_a.setObjectName("goal_a")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.goal_a)
        self.goal_b = QtWidgets.QLineEdit(position_command_layout)
        self.goal_b.setObjectName("goal_b")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.FieldRole, self.goal_b)
        self.buttonBox = QtWidgets.QDialogButtonBox(position_command_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(
            12, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.label_2 = QtWidgets.QLabel(position_command_layout)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(position_command_layout)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(position_command_layout)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(position_command_layout)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(position_command_layout)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            9, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label = QtWidgets.QLabel(position_command_layout)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.goal_speed = QtWidgets.QLineEdit(position_command_layout)
        self.goal_speed.setObjectName("goal_speed")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.goal_speed)
        self.label_7 = QtWidgets.QLabel(position_command_layout)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.relative = QtWidgets.QCheckBox(position_command_layout)
        self.relative.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.relative.setObjectName("relative")
        self.horizontalLayout.addWidget(self.relative)
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(position_command_layout)
        self.buttonBox.accepted.connect(position_command_layout.accept)
        self.buttonBox.rejected.connect(position_command_layout.reject)
        QtCore.QMetaObject.connectSlotsByName(position_command_layout)

    def retranslateUi(self, position_command_layout):
        _translate = QtCore.QCoreApplication.translate
        position_command_layout.setWindowTitle(
            _translate("position_command_layout", "Goal position"))
        self.label_2.setText(_translate("position_command_layout", "x"))
        self.label_3.setText(_translate("position_command_layout", "y"))
        self.label_4.setText(_translate("position_command_layout", "z"))
        self.label_5.setText(_translate("position_command_layout", "a"))
        self.label_6.setText(_translate("position_command_layout", "b"))
        self.label.setText(_translate("position_command_layout", "Goal"))
        self.goal_speed.setText(_translate("position_command_layout", "0"))
        self.label_7.setText(_translate("position_command_layout", "Speed"))
        self.relative.setText(_translate(
            "position_command_layout", "Relative"))
