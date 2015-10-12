#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import wx
import config
from racm_ui_main_frame import MainFrame as InheritedMainFrame

__author__ = 'mikan'

_VERSION = "0.1"


def _open_window(cfg):
    app = wx.App()
    frame = InheritedMainFrame(None, _VERSION, cfg)
    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()


def main():
    print("Remote ADB Connection Manager")
    cfg = config.RacmConfig()
    if cfg.dict is None:
        message = "Failed to create configuration file: " + cfg.get_config_path()
        wx.MessageDialog(None, message, "ERROR", wx.OK | wx.ICON_ERROR).Show()
        exit(0)
    _open_window(cfg)


if __name__ == '__main__':
    main()
