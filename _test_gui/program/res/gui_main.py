"""Subclass of pyhelper_gui, which is generated by wxFormBuilder."""

import wx
import gui

import gui_dialogpost as Pdialog
import gui_dialogfile as Fdialog

# Implementing pyhelper_gui
class pyhelperpyhelper_gui( gui.pyhelper_gui ):
	def __init__( self, parent ):
		gui.pyhelper_gui.__init__( self, parent )
	
	# Handlers for pyhelper_gui events.
	def onOutFile( self, event ):
		# TODO: Implement onOutFile
		pass
	
	def onTogglePost( self, event ):
		# TODO: Implement onTogglePost
		pass
	
	def cf_dialogfile( self, event ):
		# TODO: Implement cf_dialogfile
		dia = Fdialog.pyhelpercf_dialogfile( None )
		dia.ShowModal()
		dia.Destroy()
	
	def cf_dialogpost( self, event ):
		# TODO: Implement cf_dialogpost
		dia = Pdialog.pyhelpercf_dialogpost( None )
		dia.ShowModal()
		dia.Destroy()
	
	