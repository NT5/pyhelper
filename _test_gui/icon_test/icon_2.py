import wx
 ########################################################################
class CustomTaskBarIcon(wx.TaskBarIcon):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, frame):
        """Constructor"""
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
 
        img = wx.Image("icon.ico", wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)
        self.icon = wx.EmptyIcon()
        self.icon.CopyFromBitmap(bmp)
 
        self.SetIcon(self.icon, "Restore")
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
 
    #----------------------------------------------------------------------
    def OnTaskBarActivate(self, evt):
        """"""
        pass
 
    #----------------------------------------------------------------------
    def OnTaskBarClose(self, evt):
        """
        Destroy the taskbar icon and frame from the taskbar icon itself
        """
        self.frame.Close()
 
    #----------------------------------------------------------------------
    def OnTaskBarLeftClick(self, evt):
        """
        Create the right-click menu
        """
        self.frame.Show()
########################################################################
class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Minimize to Tray")
        panel = wx.Panel(self)
        self.tbIcon = CustomTaskBarIcon(self)
 
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)
 
        self.Show()
 
    #----------------------------------------------------------------------
    def onClose(self, evt):
        """
        Destroy the taskbar icon and the frame
        """
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()
 
    #----------------------------------------------------------------------
    def onMinimize(self, event):
        """
        When minimizing, hide the frame so it "minimizes to tray"
        """
        self.Hide()
 
#----------------------------------------------------------------------
def main():
    """"""
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
 
if __name__ == "__main__":
    main()