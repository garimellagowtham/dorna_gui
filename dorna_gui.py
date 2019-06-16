#!/usr/bin/env python
import sys
from dorna_gui_layout import Ui_dorna_main_gui
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui_logic import GUILogic
from robot_manager import DornaManager
from dorna import Dorna

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui_window = QMainWindow()
    gui_layout = Ui_dorna_main_gui()
    gui_layout.setupUi(gui_window)
    robot = Dorna()
    with DornaManager(robot):
        gui_logic = GUILogic(gui_layout, gui_window, robot)
        gui_window.show()
        sys.exit(app.exec_())
