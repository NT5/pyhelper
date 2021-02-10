#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-

import wx
import pyhelperpyhelper_gui as gui


if __name__ == "__main__":

	app = wx.App(False)
	frame = gui.pyhelperpyhelper_gui( None )

	frame.Show( True )
	app.MainLoop()