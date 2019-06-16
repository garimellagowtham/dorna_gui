#!/usr/bin/env python
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QTextCursor
from io import StringIO


class Logger(object):
    """
    Find a way to implement/use
    GLOG style print statements :)
    """
    _text_box = None
    _buffer_size = 100
    _timer_delta = 1000

    @classmethod
    def initialize(self, text_box):
        self._text_box = text_box
        self.print_buffer = []
        self.print_timer = QTimer()
        self.print_timer.timeout.connect(self.update_log)
        self.print_timer.start(self._timer_delta)

    @classmethod
    def update_log(self):
        copy_buffer = list(self.print_buffer)
        self._text_box.moveCursor(QTextCursor.End)
        for message in self.print_buffer:
            self._text_box.append(message)
        N = len(copy_buffer)
        self.print_buffer = self.print_buffer[N:]

    @classmethod
    def log(self, *args, **kwargs):
        if self._text_box is None:
            print(*args, **kwargs)
            return
        string_io = StringIO()
        kwargs['file'] = string_io
        kwargs['end'] = ''
        print(*args, **kwargs)
        if len(self.print_buffer) < self._buffer_size:
            self.print_buffer.append(string_io.getvalue())
        string_io.close()
