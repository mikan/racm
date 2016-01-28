# -*- coding: utf-8 -*-

import wx
import threading
import sys


class LogCatThread(threading.Thread):
    """"LogCat Thread"""

    _process = None
    _buff = []

    def __init__(self, adb, host, display):
        super(LogCatThread, self).__init__()
        self._adb = adb
        self._host = host
        self._display = display
        self._ready_event = threading.Event()
        self._flush_lock = threading.Lock()

    def run(self):
        """Runs on worker thread."""
        print ("[LogCat] Started.")
        self._process = self._adb.logcat(self._host)
        sys.stdout.write("[LogCat] Buffering.")
        chars = []
        while True:
            ch = self._process.stdout.read(1)  # Reads data without buffering
            if ch:
                if ch in ['\r', '\n']:
                    line = "".join(chars).decode('utf-8').rstrip()
                    if not chars:
                        continue
                    chars = []
                    line += "\n"
                    if not self._ready_event.is_set():  # Buffering
                        self._buff.append(line)
                        if len(self._buff) % 100 == 0:
                            sys.stdout.write(".")
                    elif self._buff is not None:
                        self.synchronized_flush("worker thread")
                    else:
                        wx.CallAfter(self.update, line)  # Direct output
                else:
                    chars.append(str(ch))
            else:
                break

        print ("[LogCat] Stopped.")

    def update(self, text):
        """Invoked from UI thread.
        :param text: append text
        """
        self._display.AppendText(text)

    def ready(self):
        """Start log display."""
        self._ready_event.set()
        print (" done.")
        self.synchronized_flush("UI thread")

    def stop(self):
        """Invoked from UI thread."""
        self._process.kill()

    def synchronized_flush(self, thread_name):
        """Flush buffered logs.
        :param thread_name: Name of caller thread
        """
        self._flush_lock.acquire()
        try:
            if self._buff is not None:
                self.update("".join(self._buff))
                self._buff = None
                print ("[LogCat] Buffer flushed in " + thread_name + ".")
        finally:
            self._flush_lock.release()
