# -*- coding: utf-8 -*-

import subprocess
from compiler.ast import flatten


class Adb(object):
    _path = None

    def __init__(self, path):
        self._path = path

    @staticmethod
    def _run(args):
        p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=False)
        ret = p.wait()
        output = Adb._out2str(p.stdout.readlines())
        error = Adb._out2str(p.stderr.readlines())
        print("return: " + str(ret))
        print("output: " + output)
        print("error:  " + error)
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

    def restart(self):
        self._run([self._path, "kill-server"])
        return self._run([self._path, "start-server"])
