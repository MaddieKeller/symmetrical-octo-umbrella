import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)

        sc = wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70, 25))
        self.valueText = wx.StaticText(panel, label='', pos=(130,80))

        sc.Bind(wx.EVT_SPINCTRL, self.spinControl)

    def spinControl(self, event):
        # Get spin control value
        value = event.GetPosition()
        # Update static text
        self.valueText.SetLabel(str(value))

app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()