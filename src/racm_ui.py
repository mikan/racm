# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 16 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Remote ADB Connection Manager"), pos = wx.DefaultPosition, size = wx.Size( 550,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 540,420 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		self.menu_bar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.add_menu_item = wx.MenuItem( self.file_menu, wx.ID_ANY, _(u"Add..."), _(u"Add a new target."), wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.add_menu_item )
		
		self.refresh_menu_item = wx.MenuItem( self.file_menu, wx.ID_ANY, _(u"Refresh"), _(u"Execute \"kill-server\" and \"start-server\"."), wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.refresh_menu_item )
		
		self.exit_menu_item = wx.MenuItem( self.file_menu, wx.ID_ANY, _(u"Exit"), _(u"Exit this application."), wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.exit_menu_item )
		
		self.menu_bar.Append( self.file_menu, _(u"File") ) 
		
		self.edit_menu = wx.Menu()
		self.settings_menu_item = wx.MenuItem( self.edit_menu, wx.ID_ANY, _(u"Settings..."), _(u"Change ADB path, custom buttons, and more."), wx.ITEM_NORMAL )
		self.edit_menu.AppendItem( self.settings_menu_item )
		
		self.edit_menu_item = wx.MenuItem( self.edit_menu, wx.ID_ANY, _(u"Edit..."), _(u"Edit the selected target."), wx.ITEM_NORMAL )
		self.edit_menu.AppendItem( self.edit_menu_item )
		
		self.remove_menu_item = wx.MenuItem( self.edit_menu, wx.ID_ANY, _(u"Remove"), _(u"Remove the selected target."), wx.ITEM_NORMAL )
		self.edit_menu.AppendItem( self.remove_menu_item )
		
		self.menu_bar.Append( self.edit_menu, _(u"Edit") ) 
		
		self.help_menu = wx.Menu()
		self.about_menu_item = wx.MenuItem( self.help_menu, wx.ID_ANY, _(u"About..."), _(u"About this application."), wx.ITEM_NORMAL )
		self.help_menu.AppendItem( self.about_menu_item )
		
		self.menu_bar.Append( self.help_menu, _(u"Help") ) 
		
		self.SetMenuBar( self.menu_bar )
		
		wrapper = wx.BoxSizer( wx.HORIZONTAL )
		
		self.host_list = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.host_column = self.host_list.AppendTextColumn( _(u"Host") ) 
		self.name_column = self.host_list.AppendTextColumn( _(u"Name") ) 
		self.status_column = self.host_list.AppendTextColumn( _(u"Status") ) 
		wrapper.Add( self.host_list, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		list_area_box = wx.BoxSizer( wx.VERTICAL )
		
		connection_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Connection") ), wx.VERTICAL )
		
		self.connect_button = wx.Button( self, wx.ID_ANY, _(u"Connect"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.connect_button.Enable( False )
		
		connection_box.Add( self.connect_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.disconnect_button = wx.Button( self, wx.ID_ANY, _(u"Disconnect"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.disconnect_button.Enable( False )
		
		connection_box.Add( self.disconnect_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		list_area_box.Add( connection_box, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		shell_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Shell") ), wx.VERTICAL )
		
		self.custom1_button = wx.Button( self, wx.ID_ANY, _(u"Custom 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom1_button.Enable( False )
		
		shell_box.Add( self.custom1_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.custom2_button = wx.Button( self, wx.ID_ANY, _(u"Custom 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom2_button.Enable( False )
		
		shell_box.Add( self.custom2_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.custom3_button = wx.Button( self, wx.ID_ANY, _(u"Custom 3"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom3_button.Enable( False )
		
		shell_box.Add( self.custom3_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.shell_button = wx.Button( self, wx.ID_ANY, _(u"Shell..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.shell_button.Enable( False )
		self.shell_button.Hide()
		
		shell_box.Add( self.shell_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		list_area_box.Add( shell_box, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		add_remove_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Add/Remove") ), wx.VERTICAL )
		
		self.add_button = wx.Button( self, wx.ID_ANY, _(u"Add..."), wx.DefaultPosition, wx.DefaultSize, 0 )
		add_remove_box.Add( self.add_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.remove_button = wx.Button( self, wx.ID_ANY, _(u"Remove"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.remove_button.Enable( False )
		
		add_remove_box.Add( self.remove_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		list_area_box.Add( add_remove_box, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		wrapper.Add( list_area_box, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( wrapper )
		self.Layout()
		self.status_bar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_main_closed )
		self.Bind( wx.EVT_MENU, self.on_add_selected, id = self.add_menu_item.GetId() )
		self.Bind( wx.EVT_MENU, self.on_refresh_selected, id = self.refresh_menu_item.GetId() )
		self.Bind( wx.EVT_MENU, self.on_exit_selected, id = self.exit_menu_item.GetId() )
		self.Bind( wx.EVT_MENU, self.on_settings_selected, id = self.settings_menu_item.GetId() )
		self.Bind( wx.EVT_MENU, self.on_edit_selected, id = self.edit_menu_item.GetId() )
		self.Bind( wx.EVT_MENU, self.on_remove_selected, id = self.remove_menu_item.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about_selected, id = self.about_menu_item.GetId() )
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.on_host_selection_item_activated, id = wx.ID_ANY )
		self.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.on_host_selection_changed, id = wx.ID_ANY )
		self.connect_button.Bind( wx.EVT_BUTTON, self.on_connect_clicked )
		self.disconnect_button.Bind( wx.EVT_BUTTON, self.on_disconnect_clicked )
		self.custom1_button.Bind( wx.EVT_BUTTON, self.on_custom1_clicked )
		self.custom2_button.Bind( wx.EVT_BUTTON, self.on_custom2_clicked )
		self.custom3_button.Bind( wx.EVT_BUTTON, self.on_custom3_clicked )
		self.shell_button.Bind( wx.EVT_BUTTON, self.on_shell_clicked )
		self.add_button.Bind( wx.EVT_BUTTON, self.on_add_clicked )
		self.remove_button.Bind( wx.EVT_BUTTON, self.on_remove_clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_main_closed( self, event ):
		pass
	
	def on_add_selected( self, event ):
		pass
	
	def on_refresh_selected( self, event ):
		pass
	
	def on_exit_selected( self, event ):
		pass
	
	def on_settings_selected( self, event ):
		pass
	
	def on_edit_selected( self, event ):
		pass
	
	def on_remove_selected( self, event ):
		pass
	
	def on_about_selected( self, event ):
		pass
	
	def on_host_selection_item_activated( self, event ):
		pass
	
	def on_host_selection_changed( self, event ):
		pass
	
	def on_connect_clicked( self, event ):
		pass
	
	def on_disconnect_clicked( self, event ):
		pass
	
	def on_custom1_clicked( self, event ):
		pass
	
	def on_custom2_clicked( self, event ):
		pass
	
	def on_custom3_clicked( self, event ):
		pass
	
	def on_shell_clicked( self, event ):
		pass
	
	def on_add_clicked( self, event ):
		pass
	
	def on_remove_clicked( self, event ):
		pass
	

###########################################################################
## Class SettingsFrame
###########################################################################

class SettingsFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Settings"), pos = wx.DefaultPosition, size = wx.Size( 502,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		wrapper = wx.BoxSizer( wx.VERTICAL )
		
		self.settings_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.path_panel = wx.Panel( self.settings_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		path_wrapper = wx.BoxSizer( wx.VERTICAL )
		
		adb_box = wx.StaticBoxSizer( wx.StaticBox( self.path_panel, wx.ID_ANY, _(u"ADB") ), wx.VERTICAL )
		
		self.adb_desc_text = wx.StaticText( self.path_panel, wx.ID_ANY, _(u"Path to ADB command:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.adb_desc_text.Wrap( -1 )
		adb_box.Add( self.adb_desc_text, 0, wx.ALL, 5 )
		
		self.adb_file_picker = wx.FilePickerCtrl( self.path_panel, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		adb_box.Add( self.adb_file_picker, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		adb_box.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.adb_hint_text = wx.StaticText( self.path_panel, wx.ID_ANY, _(u"Hint:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.adb_hint_text.Wrap( -1 )
		adb_box.Add( self.adb_hint_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.adb_hint1_text = wx.StaticText( self.path_panel, wx.ID_ANY, _(u"ADB command localed in \"platform-tools\" directory in the sdk home path."), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.adb_hint1_text.Wrap( -1 )
		adb_box.Add( self.adb_hint1_text, 0, wx.ALL, 5 )
		
		
		path_wrapper.Add( adb_box, 1, wx.EXPAND, 5 )
		
		
		self.path_panel.SetSizer( path_wrapper )
		self.path_panel.Layout()
		path_wrapper.Fit( self.path_panel )
		self.settings_notebook.AddPage( self.path_panel, _(u"Path"), False )
		self.custom_buttons_panel = wx.Panel( self.settings_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		custom_buttons_wrapper = wx.BoxSizer( wx.VERTICAL )
		
		self.buttons_guide_label = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"Label, enable/disable and command:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buttons_guide_label.Wrap( -1 )
		custom_buttons_wrapper.Add( self.buttons_guide_label, 0, wx.ALL, 5 )
		
		custom_buttons_grid = wx.FlexGridSizer( 3, 4, 10, 0 )
		custom_buttons_grid.AddGrowableCol( 3 )
		custom_buttons_grid.SetFlexibleDirection( wx.BOTH )
		custom_buttons_grid.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.custom1_text = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"Custom 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom1_text.Wrap( -1 )
		custom_buttons_grid.Add( self.custom1_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom1_label = wx.TextCtrl( self.custom_buttons_panel, wx.ID_ANY, _(u"Custom 1"), wx.DefaultPosition, wx.DefaultSize, 0 )
		custom_buttons_grid.Add( self.custom1_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom1_enable = wx.CheckBox( self.custom_buttons_panel, wx.ID_ANY, _(u"Enable"), wx.DefaultPosition, wx.DefaultSize, 0 )
		custom_buttons_grid.Add( self.custom1_enable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom1_command = wx.TextCtrl( self.custom_buttons_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom1_command.Enable( False )
		
		custom_buttons_grid.Add( self.custom1_command, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.custom2_text = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"Custom 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom2_text.Wrap( -1 )
		custom_buttons_grid.Add( self.custom2_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom2_label = wx.TextCtrl( self.custom_buttons_panel, wx.ID_ANY, _(u"Custom 2"), wx.DefaultPosition, wx.DefaultSize, 0 )
		custom_buttons_grid.Add( self.custom2_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom2_enable = wx.CheckBox( self.custom_buttons_panel, wx.ID_ANY, _(u"Enable"), wx.DefaultPosition, wx.DefaultSize, 0 )
		custom_buttons_grid.Add( self.custom2_enable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom2_command = wx.TextCtrl( self.custom_buttons_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom2_command.Enable( False )
		
		custom_buttons_grid.Add( self.custom2_command, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.custom3_text = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"Custom 3"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom3_text.Wrap( -1 )
		custom_buttons_grid.Add( self.custom3_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom3_label = wx.TextCtrl( self.custom_buttons_panel, wx.ID_ANY, _(u"Custom 3"), wx.DefaultPosition, wx.DefaultSize, 0 )
		custom_buttons_grid.Add( self.custom3_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom3_enable = wx.CheckBox( self.custom_buttons_panel, wx.ID_ANY, _(u"Enable"), wx.DefaultPosition, wx.DefaultSize, 0 )
		custom_buttons_grid.Add( self.custom3_enable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.custom3_command = wx.TextCtrl( self.custom_buttons_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom3_command.Enable( False )
		
		custom_buttons_grid.Add( self.custom3_command, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		custom_buttons_wrapper.Add( custom_buttons_grid, 0, wx.EXPAND, 5 )
		
		
		custom_buttons_wrapper.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.com_hint_text = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"Command examples:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.com_hint_text.Wrap( -1 )
		custom_buttons_wrapper.Add( self.com_hint_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.com_hint1_text = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"uninstall com.foo.app"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.com_hint1_text.Wrap( -1 )
		custom_buttons_wrapper.Add( self.com_hint1_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.com_hint2_text = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"shell chmod 777 /data/foo"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.com_hint2_text.Wrap( -1 )
		custom_buttons_wrapper.Add( self.com_hint2_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.com_hint3_text = wx.StaticText( self.custom_buttons_panel, wx.ID_ANY, _(u"shell am start -a android.intent.action.VIEW -d http://google.com"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.com_hint3_text.Wrap( -1 )
		custom_buttons_wrapper.Add( self.com_hint3_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.adb_command_hyperlink = wx.HyperlinkCtrl( self.custom_buttons_panel, wx.ID_ANY, _(u"ADB Shell Commands | Android Developers"), u"https://developer.android.com/tools/help/shell.html", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		custom_buttons_wrapper.Add( self.adb_command_hyperlink, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.custom_buttons_panel.SetSizer( custom_buttons_wrapper )
		self.custom_buttons_panel.Layout()
		custom_buttons_wrapper.Fit( self.custom_buttons_panel )
		self.settings_notebook.AddPage( self.custom_buttons_panel, _(u"Custom Buttons"), False )
		
		wrapper.Add( self.settings_notebook, 1, wx.ALL|wx.EXPAND, 5 )
		
		button_box = wx.BoxSizer( wx.HORIZONTAL )
		
		
		button_box.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		button_box.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.ok_button = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		button_box.Add( self.ok_button, 0, wx.ALL, 5 )
		
		
		wrapper.Add( button_box, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( wrapper )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.adb_file_picker.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_adb_path_changed )
		self.custom1_enable.Bind( wx.EVT_CHECKBOX, self.on_custom1_enable_changed )
		self.custom2_enable.Bind( wx.EVT_CHECKBOX, self.on_custom2_enable_changed )
		self.custom3_enable.Bind( wx.EVT_CHECKBOX, self.on_custom3_enable_changed )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.on_cancel_clicked )
		self.ok_button.Bind( wx.EVT_BUTTON, self.on_ok_clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_adb_path_changed( self, event ):
		pass
	
	def on_custom1_enable_changed( self, event ):
		pass
	
	def on_custom2_enable_changed( self, event ):
		pass
	
	def on_custom3_enable_changed( self, event ):
		pass
	
	def on_cancel_clicked( self, event ):
		pass
	
	def on_ok_clicked( self, event ):
		pass
	

###########################################################################
## Class AddDialog
###########################################################################

class AddDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Add a target"), pos = wx.DefaultPosition, size = wx.Size( 230,300 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		wrapper = wx.BoxSizer( wx.VERTICAL )
		
		add = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Add") ), wx.VERTICAL )
		
		self.host_text_label = wx.StaticText( self, wx.ID_ANY, _(u"Host (name or IP address):"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.host_text_label.Wrap( -1 )
		add.Add( self.host_text_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.host_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		add.Add( self.host_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.port_text_label = wx.StaticText( self, wx.ID_ANY, _(u"Port:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.port_text_label.Wrap( -1 )
		add.Add( self.port_text_label, 0, wx.ALL, 5 )
		
		self.port_text = wx.TextCtrl( self, wx.ID_ANY, _(u"5555"), wx.DefaultPosition, wx.DefaultSize, 0 )
		add.Add( self.port_text, 0, wx.ALL, 5 )
		
		self.name_label = wx.StaticText( self, wx.ID_ANY, _(u"Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_label.Wrap( -1 )
		add.Add( self.name_label, 0, wx.ALL, 5 )
		
		self.name_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		add.Add( self.name_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		wrapper.Add( add, 1, wx.EXPAND, 5 )
		
		buttons_area_box = wx.BoxSizer( wx.HORIZONTAL )
		
		
		buttons_area_box.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ok_button = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons_area_box.Add( self.ok_button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cancel_button.Hide()
		
		buttons_area_box.Add( self.cancel_button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		buttons_area_box.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		
		wrapper.Add( buttons_area_box, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( wrapper )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ok_button.Bind( wx.EVT_BUTTON, self.on_ok_clicked )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.on_cancel_clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_ok_clicked( self, event ):
		pass
	
	def on_cancel_clicked( self, event ):
		pass
	

###########################################################################
## Class EditDialog
###########################################################################

class EditDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Edit the target"), pos = wx.DefaultPosition, size = wx.Size( 230,300 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		wrapper = wx.BoxSizer( wx.VERTICAL )
		
		edit = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Edit") ), wx.VERTICAL )
		
		self.host_text_label = wx.StaticText( self, wx.ID_ANY, _(u"Host (name or IP address):"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.host_text_label.Wrap( -1 )
		edit.Add( self.host_text_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.host_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		edit.Add( self.host_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.port_text_label = wx.StaticText( self, wx.ID_ANY, _(u"Port:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.port_text_label.Wrap( -1 )
		edit.Add( self.port_text_label, 0, wx.ALL, 5 )
		
		self.port_text = wx.TextCtrl( self, wx.ID_ANY, _(u"5555"), wx.DefaultPosition, wx.DefaultSize, 0 )
		edit.Add( self.port_text, 0, wx.ALL, 5 )
		
		self.name_label = wx.StaticText( self, wx.ID_ANY, _(u"Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_label.Wrap( -1 )
		edit.Add( self.name_label, 0, wx.ALL, 5 )
		
		self.name_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		edit.Add( self.name_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		wrapper.Add( edit, 1, wx.EXPAND, 5 )
		
		buttons_area_box = wx.BoxSizer( wx.HORIZONTAL )
		
		
		buttons_area_box.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ok_button = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		buttons_area_box.Add( self.ok_button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cancel_button.Hide()
		
		buttons_area_box.Add( self.cancel_button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		buttons_area_box.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		
		wrapper.Add( buttons_area_box, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( wrapper )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ok_button.Bind( wx.EVT_BUTTON, self.on_ok_clicked )
		self.cancel_button.Bind( wx.EVT_BUTTON, self.on_cancel_clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_ok_clicked( self, event ):
		pass
	
	def on_cancel_clicked( self, event ):
		pass
	

