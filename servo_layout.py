# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servo_layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_servo_layout(object):
    def setupUi(self, servo_layout):
        servo_layout.setObjectName("servo_layout")
        servo_layout.resize(320, 240)
        self.buttonBox = QtWidgets.QDialogButtonBox(servo_layout)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.servo_slider = QtWidgets.QSlider(servo_layout)
        self.servo_slider.setGeometry(QtCore.QRect(19, 90, 291, 20))
        self.servo_slider.setMinimum(200)
        self.servo_slider.setMaximum(800)
        self.servo_slider.setSingleStep(50)
        self.servo_slider.setSliderPosition(500)
        self.servo_slider.setOrientation(QtCore.Qt.Horizontal)
        self.servo_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.servo_slider.setTickInterval(50)
        self.servo_slider.setObjectName("servo_slider")
        self.label = QtWidgets.QLabel(servo_layout)
        self.label.setGeometry(QtCore.QRect(10, 120, 59, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(servo_layout)
        self.label_2.setGeometry(QtCore.QRect(270, 120, 59, 15))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(servo_layout)
        self.buttonBox.accepted.connect(servo_layout.accept)
        self.buttonBox.rejected.connect(servo_layout.reject)
        QtCore.QMetaObject.connectSlotsByName(servo_layout)

    def retranslateUi(self, servo_layout):
        _translate = QtCore.QCoreApplication.translate
        servo_layout.setWindowTitle(_translate("servo_layout", "Dialog"))
        self.label.setText(_translate("servo_layout", "Closed"))
        self.label_2.setText(_translate("servo_layout", "Open"))

