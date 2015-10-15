#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import wx
import config
from racm_ui_main_frame import MainFrame as InheritedMainFrame

__author__ = 'mikan'

_VERSION = "0.2"


def _open_window(cfg, title):
    app = wx.App()
    frame = InheritedMainFrame(None, _VERSION, cfg, title)
    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()


def main():
    title = "Remote ADB Connection Manager v" + _VERSION
    cfg = config.RacmConfig()
    if cfg.dict is None:
        message = "Failed to create configuration file: " + cfg.get_config_path()
        wx.MessageDialog(None, message, "ERROR", wx.OK | wx.ICON_ERROR).Show()
        exit(0)
    _open_window(cfg, title)


if __name__ == '__main__':
    main()
