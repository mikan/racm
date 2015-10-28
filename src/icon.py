# -*- coding: utf-8 -*-

import wx
import platform
import os.path


def get_icon():
    if platform.system() is "Windows":
        import win32api
        return wx.Icon(win32api.GetModuleFileName(win32api.GetModuleHandle(None)), wx.BITMAP_TYPE_ICO)
    elif os.path.exists("racm.icns"):
        _icon = wx.EmptyIcon()
        return _icon
    else:
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("../resources/icons/favicon.ico", wx.BITMAP_TYPE_ANY))
        return _icon
