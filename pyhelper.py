#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-

import wx

import gui.pyhelper_pyhelper_gui as gui
import threading, sys, time, json, urllib, httplib, codecs

from gui.libs.osu_np import Listener as osunp

class program_handler:
	def __init__(self, gui):
		self.gui = gui
		self.np = {
			"core": osunp( self.osu_handler ),
			"last": {}
		}
		
		self.Threads = [ ]
		
		self.Threads.append( threading.Thread(target=self.np["core"].start) )
		
		for thr in self.Threads:
			thr.setDaemon(True)
			thr.start()
			time.sleep(0.5)
			
		print "[+] %i Threads running" % len( self.Threads )
		
		self.gui.out_text.SetValue("None")
		
	def osu_handler( self, data ):
		def parse_status( id ):
			if id == 0: return "Playing"
			elif id == 1: return "Watching"
			else: return "Listening"
			
		def make_post( vars ):
			try:
				param = urllib.urlencode( vars )
				headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
				
				conn = httplib.HTTPConnection(self.gui._configfile['np']['post']['host'])
				conn.request("POST", self.gui._configfile['np']['post']['url'], param, headers)
				
				response = conn.getresponse()
				response.read()
				conn.close()
			except Exception, e:
				print "[-] Post Error: "+str(e)
			
		song_body = []
		
		if data and self.np['last'] != data:
			self.np['last'] = data
			if data['name']: song_body.append( data['name'] )
			if data['artist']: song_body.append( data['artist'] )
			if data['difficulty']: song_body.append( "[%s]" % data['difficulty'] )

			self.gui.out_text.SetValue( "%s: %s" % ( parse_status( data['action'] ), " ".join( song_body ) ) )
			print "%s: %s" % ( parse_status( data['action'] ), " ".join( song_body ))
			
			if  self.gui._configfile['np']['file']['enable']:
				try:
					with codecs.open( self.gui._configfile['np']['file']['name'], 'w', encoding='utf8') as f:
						f.write( "%s: %s" % (parse_status( data['action'] ), " ".join( song_body ) ))
				except Exception, e:
					print "[-] File Error: "+str(e)
					
			if self.gui._configfile['np']['post']['enable']:
				post_vars = { }
				
				if len(self.gui._configfile['np']['post']['key']) > 0: post_vars.setdefault( "key", self.gui._configfile['np']['post']['key'] )
				if len( song_body ) > 0: post_vars.setdefault( "output", "%s: %s" % (parse_status( data['action'] ), " ".join( song_body )) )
				
				thr_post = threading.Thread(target=make_post, args=(post_vars,))
				thr_post.setDaemon(True)
				thr_post.start()

if __name__ == "__main__":

	app = wx.App( redirect=False )

	program = gui.pyhelper_pyhelper_gui( None )
	
	_class_handler = program_handler( program )

	program.Show( True )
	app.MainLoop()
	
