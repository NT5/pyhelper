#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-

from res.osu_np import Listener as osunp
from res.keyboard_hook import key_hook as khook

import threading, sys, time, json, urllib, httplib, codecs, threading
	
class pyhelper:
	def __init__(self, config):
		self.config = config
		self.np = {
			"core": osunp( self.osu_handler ),
			"config": self.config.get("np"),
			"last": { "data": {}, "post": 0 }
		}
		self.key_hook = {
			"core": khook( self.key_hook_handler ),
			"config": self.config.get("key_hook"),
			"listen_keys": { }
		}
		
		self.Threads = [ ]
		
		if self.np['config']:
			self.Threads.append( threading.Thread(target=self.np["core"].start) )
			
		if self.key_hook['config']:
			for key in self.key_hook['config']['keys']:
				self.key_hook['listen_keys'].setdefault( ord(key), { 'count': 0 } )
			self.Threads.append( threading.Thread(target=self.key_hook["core"].start) )
			
		for thr in self.Threads:
			thr.setDaemon(True)
			thr.start()
			time.sleep(0.5)

		print "[+] %i Threads running" % len( self.Threads )
	
	def key_hook_handler(self, e):
		if self.key_hook['listen_keys'].get( e.key_code ):
			if e.event_type == "key up":
				self.key_hook['listen_keys'][ e.key_code ]['count'] += 1
				# print "Key: %s - Count: %i" % ( chr( e.key_code ), self.key_hook['listen_keys'][ e.key_code ]['count'] )

	def key_hook_handler_end_key(self):
		_keyr = []
		for key in list(self.key_hook['listen_keys']):
			if self.key_hook['listen_keys'][ key ]['count'] > 0:
				print "Key: %s - Count: %i" % ( chr( key ), self.key_hook['listen_keys'][ key ]['count'] )
				_keyr.append( "Key %s: %s" % (chr( key ), self.key_hook['listen_keys'][ key ]['count'] ) )
				self.key_hook['listen_keys'][ key ]['count'] = 0
		return _keyr
	
	def osu_handler( self, data ):
		def parse_status( id ):
			if id == 0: return "Playing"
			elif id == 1: return "Watching"
			else: return "Listening"
			
		def make_post( vars ):
			try:
				if int( time.time() ) - self.np['last']['post'] >= 3:		
					self.np['last']['post'] = int( time.time() )
					param = urllib.urlencode( vars )
					headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
					
					conn = httplib.HTTPConnection(self.np['config']['post']['host'])
					conn.request("POST", self.np['config']['post']['url'], param, headers)
					
					response = conn.getresponse()
					response.read()
					conn.close()
			except Exception, e:
				print "Post Error: "+str(e)
		
		if data:
			if data['player'] == "osu!":
				if data != None and data != self.np['last']['data']:
					
					self.np['last']['data'] = data
					
					song_body = []
					keys_data = []
					
					if data['name']: song_body.append( data['name'] )
					if data['artist']: song_body.append( data['artist'] )
					if data['difficulty']: song_body.append( "[%s]" % data['difficulty'] )
					
					print "%s: %s" % ( parse_status( data['action'] ), " ".join( song_body ) )
					
					if data['action'] == 0:
						keys_data = self.key_hook_handler_end_key()
					if data['action'] == 3:
						keys_data = self.key_hook_handler_end_key()
					
					if self.np['config'].get('file'):
						try:
							with codecs.open(self.np['config']['file']['name'], 'w', encoding='utf8') as f:
								f.write( "%s: %s %s" % (parse_status( data['action'] ), " ".join( song_body ), ", ".join(keys_data)) )
						except Exception, e:
							print "File Error: "+str(e)
							
						if self.np['config'].get('post'):
							post_vars = { }
							
							if len(self.np['config']['post']['key']) > 0: post_vars.setdefault( "key", self.np['config']['post']['key'] )
							if len( song_body ) > 0: post_vars.setdefault( "song", " ".join( song_body ) )
							if len( keys_data ) > 0: post_vars.setdefault( "key_press", ", ".join(keys_data) )
							
							post_vars.setdefault( "status", parse_status(data['action']) )
							
							thr_post = threading.Thread(target=make_post, args=(post_vars,))
							thr_post.setDaemon(True)
							thr_post.start()

if __name__ == "__main__":
	try:
		_config = json.loads( open("config.json").read() )
	except Exception, e:
		print "Config File error: " + str( e )
		sys.exit()
		
	py = pyhelper(_config)

	raw_input("")

	for thr in py.Threads:
		thr.join(1)

	sys.exit("Script close")
