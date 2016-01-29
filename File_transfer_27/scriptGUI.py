import wx, sqlite3, time
import scripting_27
from datetime import datetime
from pytz import timezone

global filePath, cursor, conn

class Frame(wx.Frame):
    def __init__(self):
        global filePath, cursor,conn

        wx.Frame.__init__(self, None, title = "File Transfer Application", size=(600,400))
        panel = wx.Panel(self)

        lastBox = wx.StaticBox(panel, label="Last Run On:",pos=(10,10),size=(570,75))

        #set the file_check box value to equal the last time the program was used.
        self.file_check = wx.TextCtrl(lastBox, pos=(40,30),size=(300,-1), style=wx.TE_READONLY)
        self.file_check.SetLabel(str(self.getTime()))

        #source selection
        srcBox = wx.StaticBox(panel,label="Source Folder",pos=(10,100), size=(570,75))
        self.sourcePath = wx.TextCtrl(srcBox,pos=(40,30), size=(400,-1))
        srcButton = wx.Button(srcBox,label = "Browse...", pos=(450,30))
        srcButton.Bind(wx.EVT_BUTTON, self.selectFolder)

        #destination selection
        destBox = wx.StaticBox(panel,label='Destination Folder', pos = (10,190), size=(570,75))
        self.destPath = wx.TextCtrl(destBox, pos=(40,30), size=(400,-1))

        destButton = wx.Button(destBox,label = "Browse...", pos=(450,30))
        destButton.Bind(wx.EVT_BUTTON, self.selectDest)

        #submit
        runScriptButton = wx.Button(panel,label = "Run File Transfer",pos=(250,300))
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
            scripting_27.getFiles(source, destination,self.checkAsDate)
            portland_tz=timezone("US/Pacific")
            portland_dt = portland_tz.localize(datetime.now())
            sql = "INSERT INTO fileChecktbl (file_check) VALUES ('{}');".format(portland_dt)
            conn.execute(sql)
            conn.commit()
            dlg = wx.MessageDialog(None,"Files modified or created since {} have been copied from {} to {}."
                                   .format(self.checkAsDate,source,destination))
            dlg.ShowModal()
            dlg.Destroy()
            self.sourcePath.SetLabel('')
            self.destPath.SetLabel('')
            self.file_check.SetLabel(self.getTime())
            #add in update to file_check box once added

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

    def getTime(self):
        #check the database for the last time this program was used.
        cursor = conn.execute("SELECT file_check FROM fileChecktbl ORDER BY file_check DESC LIMIT 1")
        rows = cursor.fetchall()
        for row in rows:
            self.checkAsDate = row[0]
            return row[0]

def main():
    global cursor,conn
    conn = sqlite3.connect('file_transfer.db')

    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()


if __name__=='__main__': main()