# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class pyhelper_gui
###########################################################################

class pyhelper_gui ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"osu!pynp"), pos = wx.DefaultPosition, size = wx.Size( 507,156 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		pyhelper_boxs = wx.BoxSizer( wx.VERTICAL )
		
		song_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Current Song") ), wx.VERTICAL )
		
		self.out_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 475,20 ), wx.TE_READONLY )
		song_box.Add( self.out_text, 0, wx.ALL, 5 )
		
		
		pyhelper_boxs.Add( song_box, 1, wx.EXPAND, 5 )
		
		toggles = wx.GridSizer( 0, 2, 0, 0 )
		
		self.toggle_file = wx.CheckBox( self, wx.ID_ANY, _(u"Output File"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.toggle_file.SetValue(True) 
		toggles.Add( self.toggle_file, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.toggle_post = wx.CheckBox( self, wx.ID_ANY, _(u"Toggle Post"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.toggle_post.SetValue(True) 
		toggles.Add( self.toggle_post, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		pyhelper_boxs.Add( toggles, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( pyhelper_boxs )
		self.Layout()
		self.pyhelper_menu = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menu_configfile = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"File"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menu_configfile )
		
		self.menu_configpost = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Post"), wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.menu_configpost )
		
		self.pyhelper_menu.Append( self.m_menu1, _(u"Config") ) 
		
		self.SetMenuBar( self.pyhelper_menu )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.toggle_file.Bind( wx.EVT_CHECKBOX, self.onOutFile )
		self.toggle_post.Bind( wx.EVT_CHECKBOX, self.onTogglePost )
		self.Bind( wx.EVT_MENU, self.cf_dialogfile, id = self.menu_configfile.GetId() )
		self.Bind( wx.EVT_MENU, self.cf_dialogpost, id = self.menu_configpost.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onOutFile( self, event ):
		event.Skip()
	
	def onTogglePost( self, event ):
		event.Skip()
	
	def cf_dialogfile( self, event ):
		event.Skip()
	
	def cf_dialogpost( self, event ):
		event.Skip()
	

###########################################################################
## Class cf_dialogpost
###########################################################################

class cf_dialogpost ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Post"), pos = wx.DefaultPosition, size = wx.Size( 367,187 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Config") ), wx.VERTICAL )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Key"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, _(u"123456"), wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gSizer5.Add( self.m_textCtrl4, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, _(u"Host"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		gSizer5.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, _(u"localhost:8090"), wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gSizer5.Add( self.m_textCtrl41, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, _(u"URL"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )
		gSizer5.Add( self.m_staticText511, 0, wx.ALL, 5 )
		
		self.m_textCtrl411 = wx.TextCtrl( self, wx.ID_ANY, _(u"/pyhelper"), wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gSizer5.Add( self.m_textCtrl411, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		sbSizer5.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetDefault() 
		sbSizer5.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.cf_savedata )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cf_savedata( self, event ):
		event.Skip()
	

###########################################################################
## Class cf_dialogfile
###########################################################################

class cf_dialogfile ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Output File"), pos = wx.DefaultPosition, size = wx.Size( 271,158 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sb_config = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Config") ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"File"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, u"np", _(u"Select a file"), u"*.txt", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		gSizer2.Add( self.m_filePicker1, 0, wx.ALIGN_RIGHT, 5 )
		
		
		sb_config.Add( gSizer2, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetDefault() 
		sb_config.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( sb_config )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.cf_changefile )
		self.m_button1.Bind( wx.EVT_BUTTON, self.cf_savedata )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cf_changefile( self, event ):
		event.Skip()
	
	def cf_savedata( self, event ):
		event.Skip()
	

