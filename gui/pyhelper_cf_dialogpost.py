"""Subclass of cf_dialogpost, which is generated by wxFormBuilder."""

import wx
import pyhelper_gui_form

# Implementing cf_dialogpost
class pyhelper_cf_dialogpost( pyhelper_gui_form.cf_dialogpost ):
	def __init__( self, parent ):
		pyhelper_gui_form.cf_dialogpost.__init__( self, parent )
		self._configparser = parent._configparser
		self._configfile = self._configparser.config_data
	
	# Handlers for cf_dialogpost events.
	def cf_init( self, event ):
		# TODO: Implement cf_init
		
		#Post Key
		self.m_textCtrl4.SetValue( self._configfile['np']['post']['key'] )
		#Post Host
		self.m_textCtrl41.SetValue( self._configfile['np']['post']['host'] )
		#Post URL
		self.m_textCtrl411.SetValue( self._configfile['np']['post']['url'] )
	
	def cf_savedata( self, event ):
		# TODO: Implement cf_savedata
		self._configfile['np']['post']['key'] = self.m_textCtrl4.GetValue()
		self._configfile['np']['post']['host'] = self.m_textCtrl41.GetValue()
		self._configfile['np']['post']['url'] = self.m_textCtrl411.GetValue()
		self._configparser.SaveConfig()
		self.Destroy()
	
	