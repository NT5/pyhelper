#!/usr/bin/env python
# -?- coding: UTF-8 -*-

import os.path
import json

import gettext
_ = gettext.gettext

class Configurator:
	def __init__(self):
		self.config_file = "config.json"
		self.config_data = None
		self.np_default_struct = dict(
			np = dict(
				post = dict(
					key = "12345",
					host = "localhost:8090",
					url = "/pynp",
					enable = False
				),
				file = dict(
					name = "np.txt",
					enable = True
				)
			)
		)
		
		self.CheckConfig()
		
	def CheckConfig(self):
		if os.path.isfile(self.config_file):
			print _("[+] Configuracion Encontrada...")
			self.LoadConfig()
		else:
			print _("[-] No se encontro configuracion")
			self.MakeConfig()
			
	def LoadConfig(self):
		try:
			self.config_data = json.loads( open( self.config_file ).read() )
			print _("[+] Configuracion cargada correctamente!")
		except Exception, e:
			print _("[-] Error en la configuracion: ") + str( e )
			return None
		
	def MakeConfig(self):
		try:
			with open( self.config_file, "w+") as jsonFile:
				jsonFile.seek( 0 )
				jsonFile.write( json.dumps( self.np_default_struct, sort_keys=True, indent=4 ) )
				jsonFile.truncate()
				self.config_data = self.np_default_struct
				print _("[+] Configuracion creada!")
		except:
			print _("[-] No se pudo crear la configuracion")
		
	def SaveConfig(self):
		try:
			with open( self.config_file, "r+") as jsonFile:
				jsonFile.seek( 0 )
				jsonFile.write( json.dumps( self.config_data, sort_keys=True, indent=4 ) )
				jsonFile.truncate()
				print _("[+] Configuracion guardada!")
		except:
			print _("[-] No se pudo crear la configuracion")
		