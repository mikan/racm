from unittest import TestCase
from adb import Adb
import os.path

__author__ = 'mikan'

_stub_adb = "stub_adb.py"
_python_command = "python2"
_test_target = "127.0.0.1"


class TestAdb(TestCase):
    _test_command = ""
    _adb = None

    def setUp(self):
        if os.path.exists(_stub_adb):
            self._test_command = [_python_command, _stub_adb]
        elif os.path.exists("test/" + _stub_adb):
            self._test_command = [_python_command, "test/" + _stub_adb]
        else:
            self.fail("Missing stub adb!")
        self._adb = Adb(self._test_command)

    def test__run(self):
        self.assertEqual("1", Adb._run(self._test_command))

    def test__out2str(self):
        _input = ["one", "two", "three"]
        self.assertEqual("one two three", Adb._out2str(_input))

    def test_connect(self):
        self.assertEqual("3", self._adb.connect(_test_target))

    def test_disconnect(self):
        self.assertEqual("3", self._adb.connect(_test_target))

    def test_shell(self):
        self.assertEqual("6", self._adb.shell(_test_target, "1 2 3"))

    def test_install_apk(self):
        self.assertEqual("offline", self._adb.get_state(_test_target))

    def test_get_state(self):
        self.assertEqual("offline", self._adb.get_state(_test_target))

    def test_restart(self):
        self.assertEqual("offline", self._adb.get_state(_test_target))

    def test_path_provided(self):
        self.assertTrue(self._adb.path_provided())
