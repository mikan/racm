"""Subclass of MainFrame, which is generated by wxFormBuilder."""

import wx
import adb
import racm_ui
from racm_ui_add_dialog import AddDialog as InheritedAddDialog
from racm_ui_edit_dialog import EditDialog as InheritedEditDialog
from racm_ui_settings_frame import SettingsFrame as InheritedSettingsFrame

_COLUMN_HOST = 0
_COLUMN_NAME = 1
_COLUMN_STATUS = 2


# Implementing MainFrame
class MainFrame(racm_ui.MainFrame):
    _config = None
    _adb = None
    _version = ""

    def __init__(self, parent, version, config):
        racm_ui.MainFrame.__init__(self, parent)
        self._version = version
        self._config = config
        self.apply_config()
        self.host_list.GetColumn(_COLUMN_HOST).SetWidth(120)
        self.host_list.GetColumn(_COLUMN_NAME).SetWidth(120)
        self.host_list.GetColumn(_COLUMN_STATUS).SetWidth(140)

    # Handlers for MainFrame events.
    def on_refresh_selected(self, event):
        self.SetStatusText("Restarting ADB server... Please wait.")
        ret = self._adb.restart()
        self.SetStatusText("ADB server restarted successfully." if not ret or "successfully" in ret else ret)

    def on_add_selected(self, event):
        self.on_add_clicked(event)

    def on_exit_selected(self, event):
        self.Close()

    def on_settings_selected(self, event):
        InheritedSettingsFrame(None, self, self._config).Show()

    def on_edit_selected(self, event):
        self.on_host_selection_item_activated(event)

    def on_remove_selected(self, event):
        self.on_remove_clicked(event)

    def on_about_selected(self, event):
        about = wx.AboutDialogInfo()
        about.Name = "Remote ADB Connection Manager"
        about.Version = self._version
        about.Copyright = "(C) 2015 Yutaka Kato"
        about.WebSite = "https://github.com/mikan/racm"
        wx.AboutBox(about)

    def on_host_selection_changed(self, event):
        selected = self.host_list.GetSelectedRow() >= 0
        self.connect_button.Enable(selected)
        self.disconnect_button.Enable(selected)
        self.custom1_button.Enable(selected and self._config.get_enable("custom1.enable"))
        self.custom2_button.Enable(selected and self._config.get_enable("custom2.enable"))
        self.custom3_button.Enable(selected and self._config.get_enable("custom3.enable"))
        self.shell_button.Enable(selected)
        self.remove_button.Enable(selected)

    def on_host_selection_item_activated(self, event):
        row = self.host_list.GetSelectedRow()
        if row < 0:
            self._show_error("No items selected.")
            return
        host_with_port = self.host_list.GetValue(row, _COLUMN_HOST).split(":")
        host = host_with_port[0]
        port = host_with_port[1]
        name = self.host_list.GetValue(row, _COLUMN_NAME)
        dialog = InheritedEditDialog(None, self, host, port, name, row)
        dialog.ShowModal()
        dialog.Destroy()

    def on_connect_clicked(self, event):
        row = self.host_list.GetSelectedRow()
        if row < 0:
            self._show_error("No items selected.")
            return
        self.SetStatusText("Connecting... Please wait.")
        result = self._adb.connect(self.host_list.GetValue(row, _COLUMN_HOST))
        self.host_list.SetTextValue(self._get_connect_status(result), row, _COLUMN_STATUS)
        self.SetStatusText(result)

    def on_disconnect_clicked(self, event):
        row = self.host_list.GetSelectedRow()
        if row < 0:
            self._show_error("No items selected.")
            return
        self.SetStatusText("Disconnecting... Please wait.")
        result = self._adb.disconnect(self.host_list.GetValue(row, _COLUMN_HOST))
        self.host_list.SetTextValue(self._get_disconnect_status(result), row, _COLUMN_STATUS)
        self.SetStatusText(result)

    def on_custom1_clicked(self, event):
        self._exec_adb_shell(self._config.get("custom1.command"))

    def on_custom2_clicked(self, event):
        self._exec_adb_shell(self._config.get("custom2.command"))

    def on_custom3_clicked(self, event):
        self._exec_adb_shell(self._config.get("custom3.command"))

    def on_shell_clicked(self, event):
        pass

    def on_add_clicked(self, event):
        dialog = InheritedAddDialog(None, self, self._config.get("port.default"))
        dialog.ShowModal()
        dialog.Destroy()

    def on_remove_clicked(self, event):
        row = self.host_list.GetSelectedRow()
        if row >= 0:
            self.host_list.DeleteItem(row)
            self.on_host_selection_changed(None)
        else:
            self._show_error("No items selected.")

    def apply_config(self):
        # ADB
        adb_path = self._config.get("adb.path")
        self._adb = adb.Adb(adb_path)
        if adb_path is "":
            self.SetStatusText("Please set a path to the ADB.")
        else:
            self.SetStatusText("Configuration loaded.")
        # Custom buttons
        self.custom1_button.SetLabelText(self._config.get("custom1.label"))
        self.custom2_button.SetLabelText(self._config.get("custom2.label"))
        self.custom3_button.SetLabelText(self._config.get("custom3.label"))
        # Load table contents
        self.host_list.DeleteAllItems()
        for host in self._config.get("hosts"):
            self.host_list.AppendItem([host["host"], host["name"], ""])

    def add_item(self, host, name, status):
        self.host_list.AppendItem([host, name, status])
        self._config.add_item(host, name)
        self._config.write()

    def edit_item(self, host, name, status, row):
        self.host_list.SetTextValue(host, row, _COLUMN_HOST)
        self.host_list.SetTextValue(name, row, _COLUMN_NAME)
        self.host_list.SetTextValue(status, row, _COLUMN_STATUS)
        self._config.edit_item(host, name, row)
        self._config.write()

    def _show_error(self, message):
        dialog = wx.MessageDialog(None, message, self.Title, wx.OK | wx.ICON_WARNING)
        dialog.ShowModal()
        dialog.Destroy()

    def _exec_adb_shell(self, command):
        row = self.host_list.GetSelectedRow()
        if row < 0:
            return
        self.SetStatusText("Executing shell... Please wait.")
        result = self._adb.shell(self.host_list.GetValue(row, _COLUMN_HOST), command)
        self.SetStatusText(result)
        if "device offline" in result:
            self.host_list.SetTextValue("OFFLINE", row, _COLUMN_STATUS)
            dialog = wx.MessageDialog(None, "Device is offline. Are you sure to restart ADB server?",
                                      "Device is offline", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            ret = dialog.ShowModal()
            dialog.Destroy()
            if ret == wx.ID_YES:
                self.on_refresh_selected(None)
                self._adb.shell(self.host_list.GetValue(row, _COLUMN_HOST), command)
                self.SetStatusText(result)

    @staticmethod
    def _get_connect_status(status):
        if "connected to" in status:
            return "CONNECTED"
        elif "unable to connect" in status:
            return "Unable to connect"
        return status

    @staticmethod
    def _get_disconnect_status(status):
        if not str.strip(status):
            return "DISCONNECTED"
        elif "No such device" in status:
            return "No such device"
        return status
