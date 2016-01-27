import wx
import scripting_27

global filePath

class Frame(wx.Frame):
    def __init__(self):
        global filePath

        wx.Frame.__init__(self, None, title = "File Transfer Application", size=(500,350))
        panel = wx.Panel(self)

        #source selection
        srcBox = wx.StaticBox(panel,label="Source Folder",pos=(10,10), size=(470,100))
        self.sourcePath = wx.TextCtrl(srcBox,pos=(40,30), size=(400,-1))
        srcButton = wx.Button(srcBox,label = "Get Source Folder", pos=(30,70))
        srcButton.Bind(wx.EVT_BUTTON, self.selectFolder)

        #destination selection
        destBox = wx.StaticBox(panel,label='Destination Folder', pos = (10,130), size=(470,100))
        self.destPath = wx.TextCtrl(panel, pos=(40,160), size=(400,-1))

        destButton = wx.Button(panel,label = "Get Destination Folder", pos=(30,200))
        destButton.Bind(wx.EVT_BUTTON, self.selectDest)

        #submit
        runScriptButton = wx.Button(panel,label = "Run File Transfer",pos=(200,250))
        runScriptButton.Bind(wx.EVT_BUTTON,self.scriptButton)

    def scriptButton(self,event):
        source = self.sourcePath.GetValue()
        destination = self.destPath.GetValue()

        if (source=="") or (destination==""):
            dlg = wx.MessageDialog(None,"Please select a source and destination folder.","Missing Information",wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False
        else:
            scripting_27.getFiles(source, destination)


    def selectFolder(self, event):
        global filePath
        dialog = wx.DirDialog(None,"Select Source Folder", defaultPath ='', pos=(100,50),
                              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            filePath = dialog.GetPath()
            self.sourcePath.SetLabel(filePath)
        dialog.Destroy()

    def selectDest(self, event):
        global filePath
        dialog = wx.DirDialog(None,"Select Destination Folder",defaultPath='',pos=(100,50),
                              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            filePath = dialog.GetPath()
            self.destPath.SetLabel(filePath)


def main():
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()


if __name__=='__main__': main()