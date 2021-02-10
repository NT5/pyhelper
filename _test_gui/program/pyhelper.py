#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-

import wx
import threading, sys, time, json, urllib, httplib, codecs
import res.gui_main as gui

from res.osu_np import Listener as osunp

class program_handler:
	def __init__(self, gui):
		self.gui = gui
		self.np = {
			"core": osunp( self.osu_handler )
		}
		
		self.Threads = [ ]
		
		self.Threads.append( threading.Thread(target=self.np["core"].start) )
		
		for thr in self.Threads:
			thr.setDaemon(True)
			thr.start()
			time.sleep(0.5)
		
		self.gui.out_text.SetValue("None")
		
	def osu_handler( self, data ):
	
		def parse_status( id ):
			if id == 0: return "Playing"
			elif id == 1: return "Watching"
			else: return "Listening"
			
		song_body = []
		
		if data['name']: song_body.append( data['name'] )
		if data['artist']: song_body.append( data['artist'] )
		if data['difficulty']: song_body.append( "[%s]" % data['difficulty'] )

		self.gui.out_text.SetValue( "%s: %s" % ( parse_status( data['action'] ), " ".join( song_body ) ) )
	

if __name__ == "__main__":

	def OnTaskBarRight(event):
		app.ExitMainLoop()
	
	app = wx.App( False )
	icon = wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO)

	#setup taskbar icon
	tbicon = wx.TaskBarIcon()
	tbicon.SetIcon(icon, "I am an Icon")

	#add taskbar icon event
	wx.EVT_TASKBAR_RIGHT_UP(tbicon, OnTaskBarRight)
	program = gui.pyhelperpyhelper_gui( None )
	_class_handler = program_handler( program )

	program.Show( True )
	app.MainLoop()
	
