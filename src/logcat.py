# -*- coding: utf-8 -*-

import wx
import threading


class LogCatThread(threading.Thread):
    """"LogCat Thread"""

    _process = None

    def __init__(self, adb, host, display):
        super(LogCatThread, self).__init__()
        self._adb = adb
        self._host = host
        self._display = display
        self._stop_event = threading.Event()

    def run(self):
        print ("LogCat started.")
        self._process = self._adb.logcat(self._host)
        chars = []
        count = 0
        buffer_break = 4000
        buff = []
        while True:
            ch = self._process.stdout.read(1)
            if ch:
                if ch in ['\r', '\n']:
                    line = "".join(chars).decode('utf-8').rstrip()
                    if not chars:
                        continue
                    chars = []
                    count += 1
                    print (line)
                    line += "\n"
                    if count > buffer_break:
                        wx.CallAfter(self.update, line)  # direct output
                        self._process.stdout.flush()
                    elif count == buffer_break:
                        buff.append(line)
                        wx.CallAfter(self.update, "".join(buff))  # store buffered logs
                    else:
                        buff.append(line)  # buffering
                else:
                    chars.append(str(ch))
            else:
                break

        print ("LogCat stopped.")

    def update(self, text):
        self._display.AppendText(text)

    def stop(self):
        self._stop_event.set()
        self._process.kill()
