# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vegetable_cut_layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VegetableCutLayout(object):
    def setupUi(self, VegetableCutLayout):
        VegetableCutLayout.setObjectName("VegetableCutLayout")
        VegetableCutLayout.resize(413, 323)
        self.formLayout = QtWidgets.QFormLayout(VegetableCutLayout)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(VegetableCutLayout)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(VegetableCutLayout)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.vegetable_height = QtWidgets.QLineEdit(VegetableCutLayout)
        self.vegetable_height.setObjectName("vegetable_height")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.vegetable_height)
        self.label_2 = QtWidgets.QLabel(VegetableCutLayout)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.vegetable_width = QtWidgets.QLineEdit(VegetableCutLayout)
        self.vegetable_width.setObjectName("vegetable_width")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.vegetable_width)
        self.slice_width = QtWidgets.QLineEdit(VegetableCutLayout)
        self.slice_width.setObjectName("slice_width")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.slice_width)
        self.label_4 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.stroke_length = QtWidgets.QLineEdit(VegetableCutLayout)
        self.stroke_length.setObjectName("stroke_length")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.stroke_length)
        self.label_6 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.origin_x = QtWidgets.QLineEdit(VegetableCutLayout)
        self.origin_x.setObjectName("origin_x")
        self.horizontalLayout.addWidget(self.origin_x)
        self.label_8 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.origin_y = QtWidgets.QLineEdit(VegetableCutLayout)
        self.origin_y.setObjectName("origin_y")
        self.horizontalLayout.addWidget(self.origin_y)
        self.label_9 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.origin_z = QtWidgets.QLineEdit(VegetableCutLayout)
        self.origin_z.setObjectName("origin_z")
        self.horizontalLayout.addWidget(self.origin_z)
        self.label_10 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.origin_a = QtWidgets.QLineEdit(VegetableCutLayout)
        self.origin_a.setObjectName("origin_a")
        self.horizontalLayout.addWidget(self.origin_a)
        self.label_11 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.origin_b = QtWidgets.QLineEdit(VegetableCutLayout)
        self.origin_b.setObjectName("origin_b")
        self.horizontalLayout.addWidget(self.origin_b)
        self.formLayout.setLayout(
            1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.cut_speed = QtWidgets.QLineEdit(VegetableCutLayout)
        self.cut_speed.setObjectName("cut_speed")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.cut_speed)
        self.label_12 = QtWidgets.QLabel(VegetableCutLayout)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.LabelRole, self.label_12)

        self.retranslateUi(VegetableCutLayout)
        self.buttonBox.accepted.connect(VegetableCutLayout.accept)
        self.buttonBox.rejected.connect(VegetableCutLayout.reject)
        QtCore.QMetaObject.connectSlotsByName(VegetableCutLayout)

    def retranslateUi(self, VegetableCutLayout):
        _translate = QtCore.QCoreApplication.translate
        VegetableCutLayout.setWindowTitle(_translate(
            "VegetableCutLayout", "Vegetable Cutting"))
        self.label.setText(_translate("VegetableCutLayout", "Origin"))
        self.label_2.setText(_translate(
            "VegetableCutLayout", "Vegetable Properties"))
        self.label_3.setText(_translate("VegetableCutLayout", "Height"))
        self.label_4.setText(_translate("VegetableCutLayout", "Width"))
        self.label_5.setText(_translate("VegetableCutLayout", "Slice width"))
        self.label_6.setText(_translate("VegetableCutLayout", "Stroke length"))
        self.label_7.setText(_translate("VegetableCutLayout", "x"))
        self.label_8.setText(_translate("VegetableCutLayout", "y"))
        self.label_9.setText(_translate("VegetableCutLayout", "z"))
        self.label_10.setText(_translate("VegetableCutLayout", "a"))
        self.label_11.setText(_translate("VegetableCutLayout", "b"))
        self.label_12.setText(_translate("VegetableCutLayout", "Cut speed"))
