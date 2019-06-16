#!/usr/bin/env python
from logger import Logger
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread


class ThreadWrapper(QThread):
    def __init__(self, call_function):
        self.call_function = call_function
        super(ThreadWrapper, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        self.call_function()


class SlotManager(object):
    """
    Generates a single thread to call the
    slot instead of calling in main thread.
    Also adds functionality to only allow one slot
    at a time to ensure multiple slots are not accessing
    the robot at the same time
    """
    _timer_busy = False
    _update_robot_status_fn = None
    _status_check_fn = None

    def __init__(self, slot_function, lock_timer=True,
                 initialize_fcn=None, exit_fcn=None):
        """
        Pass no_message as one of kwargs if you want to avoid showing a message
        """
        self.slot_function = slot_function
        self.lock_timer = lock_timer
        self.initialize_fcn = initialize_fcn
        self.thread = None
        self.exit_fcn = exit_fcn
        assert self._status_check_fn is not None

    @classmethod
    def set_update_robot_status_fn(self, update_robot_status_fn):
        self._update_robot_status_fn = update_robot_status_fn

    @classmethod
    def set_status_check_fn(self, status_check_fn):
        self._status_check_fn = status_check_fn

    def __call__(self, *args, **kwargs):
        """
        Takes in args corresponding to a generic slot
        and passes them to the slot function
        """

        if self.lock_timer and SlotManager._timer_busy:
            Logger.log("SlotManager: Robot is currently busy!"
                       "So cannot execute the commanded slot!")
        else:
            if self._update_robot_status_fn is not None:
                self._update_robot_status_fn()

            if not self._status_check_fn():
                Logger.log("SlotManager: Robot status failed")
            else:
                SlotManager._timer_busy = True
                if self.initialize_fcn is not None:
                    kwargs['user_input'] = self.initialize_fcn()

                # Define slot function wrapper
                def slot_function_wrapper():
                    self.slot_function(*args, **kwargs)
                    SlotManager._timer_busy = False

                def exit_function_wrapper():
                    print("Finished thread!!")
                    self.exit_fcn(*args, **kwargs)

                self.thread = ThreadWrapper(slot_function_wrapper)
                if self.exit_fcn is not None:
                    self.thread.finished.connect(exit_function_wrapper)
                self.thread.start()
