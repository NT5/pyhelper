import wx
class sysTrayDemo(wx.Frame):
	def __init__(self, parent, id, title):
		pass
		wx.Frame.__init__(self, parent, -1, title, size = (800, 600), style=wx.DEFAULT_FRAME_STYLE|wx.NO_FULL_REPAINT_ON_RESIZE)
        # FIXME: substitute your icon file here.
		icon = wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon)
		
		if wx.Platform == '__WXMSW__':
			# setup a taskbar icon, and catch some events from it
			self.tbicon = wx.TaskBarIcon()
			self.tbicon.SetIcon(icon, "SysTray Demo")
			wx.EVT_TASKBAR_LEFT_DCLICK(self.tbicon, self.OnTaskBarActivate)
			wx.EVT_TASKBAR_RIGHT_UP(self.tbicon, self.OnTaskBarMenu)
			wx.EVT_MENU(self.tbicon, self.TBMENU_RESTORE, self.OnTaskBarActivate)
			wx.EVT_MENU(self.tbicon, self.TBMENU_CLOSE, self.OnTaskBarClose)
		wx.EVT_ICONIZE(self, self.OnIconify)
		# self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
		return
		
	def OnIconify(self, evt):
		self.Hide()
		return
		
	def OnTaskBarActivate(self, evt):
		if self.IsIconized():
			self.Iconize(False)
		if not self.IsShown():
			self.Show(True)
		self.Raise()
		return
		
	def OnCloseWindow(self, event):
		if hasattr(self, "tbicon"):
			del self.tbicon
		self.Destroy()
		
	TBMENU_RESTORE = 1000
	TBMENU_CLOSE   = 1001
	
	def OnTaskBarMenu(self, evt):
		menu = wx.Menu()
		menu.Append(self.TBMENU_RESTORE, "Restore SysTray Demo")
		menu.Append(self.TBMENU_CLOSE,   "Close")
		self.tbicon.PopupMenu(menu)
		menu.Destroy()
		
	def OnTaskBarClose(self, evt):
		self.Close()
		wx.GetApp().ProcessIdle()

class MyApp(wx.App):
	def OnInit(self):
		self.redirect=True
		frame = sysTrayDemo(None, -1, "SysTray Demo")
		frame.Show(True)
		return True

def main():
	app = MyApp()
	app.MainLoop()

if __name__ == '__main__':
	main()

