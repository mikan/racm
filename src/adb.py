# -*- coding: utf-8 -*-

import subprocess
from compiler.ast import flatten


class Adb(object):
    _path = None

    def __init__(self, path):
        self._path = path

    @staticmethod
    def _startup_info():
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        return startupinfo

    @staticmethod
    def _run(args):
        p = subprocess.Popen(flatten(args), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=False, startupinfo=Adb._startup_info())
        ret = p.wait()
        output = Adb._out2str(p.stdout.readlines())
        error = Adb._out2str(p.stderr.readlines())
        print("[ADB] return: " + str(ret))
        if output:
            print("[ADB] output: " + output)
        if error:
            print("[ADB] error:  " + error)
        return output if ret is 0 else error

    @staticmethod
    def _out2str(text_seq):
        return str.strip(" ".join(text_seq).replace("\\r", "").replace("\\n", ""))

    def connect(self, host):
        return self._run([self._path, "connect", host])

    def disconnect(self, host):
        return self._run([self._path, "disconnect", host])

    def shell(self, host, command):
        args = flatten([self._path, "-s", host, command.split(" ")])
        print (args)
        return self._run(args)

    def logcat(self, host):
        args = [self._path, "-s", host, "logcat"]
        return subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                shell=False, startupinfo=Adb._startup_info())

    def install_apk(self, host, file_path):
        _state = self.get_state(host)
        if _state is "offline":
            return "device offline"
        # -r: replace existing application
        # -t: allow test packages
        # -d: allow version code downgrade
        args = [self._path, "-s", host, "install", "-rt", file_path]
        print (args)
        return self._run(args)

    def get_state(self, host):
        _state = self.shell(host, "get-state")
        if "unknown" in _state:
            return "offline"
        elif "device" in _state:
            return "online"
        else:
            return "offline"
        pass

    def restart(self):
        self._run([self._path, "kill-server"])
        return self._run([self._path, "start-server"])

    def path_provided(self):
        return self._path is not None and not self._path == ""
