import wx, db_program

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self,None,title=title, size=(800,600))
        panel = wx.Panel(self)

        #menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(),'Exit')
        menuBar.Append(fileMenu,'File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.exitProgram,exitItem)

        #add Status Bar
        self.CreateStatusBar()

        #New Character Section
        wx.StaticBox(panel,
                      label="Add a New Character",
                      size=(280,260),
                      pos=(20,40))
        wx.StaticText(panel,
                      label="Name:",
                      pos=(30,70))
        wx.StaticText(panel,
                      label="Gender:",
                      pos=(30,110))
        wx.StaticText(panel,
                      label="Age:",
                      pos=(30,170))
        wx.StaticText(panel,
                      label="Occupation:",
                      pos=(30,210))
        self.charName = wx.TextCtrl(panel,
                    size=(150,-1),
                    pos=(130,70))
        #self.charGen = wx.TextCtrl(panel, size=(150,-1), pos=(130,110))
        self.charGenF = wx.CheckBox(panel,
                    label="Female",
                    pos=(130,110))
        self.charGenM = wx.CheckBox(panel, label="Male", pos=(130,140))
        self.charAge = wx.SpinCtrl(panel,
                    value='0',
                    size=(70,25),
                    pos=(130,170))
        self.charOcc = wx.TextCtrl(panel,
                    size=(150,-1),
                    pos=(130,210))

        #new Character Button
        saveButton = wx.Button(panel, label="Add Character", pos=(100,250))
        saveButton.Bind(wx.EVT_BUTTON, self.addCharacter)  #Bind button to New Character function from db_program

        #Table setup
        self.listCnt = wx.ListCtrl(panel, size=(450,400), pos=(330,40), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.listCnt.InsertColumn(0,"ID")
        self.listCnt.InsertColumn(1,"Name")
        self.listCnt.InsertColumn(2,"Gender")
        self.listCnt.InsertColumn(3,"Age")
        self.listCnt.InsertColumn(4,"Occupation")
        self.fillListCnt()
        self.listCnt.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

        deleteBtn = wx.Button(panel, label="Delete Character", pos=(510,460))
        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

    def onSelect(self, event):
       self.selectedID = event.GetText()

    def addCharacter(self, event):
        name = self.charName.GetValue()
        if (self.charGenF == True):
            gender = "Female"
        else:
            gender = "Male"
        #gender = self.charGen.GetValue()
        age = self.charAge.GetValue()
        occupation = self.charOcc.GetValue()

        if (name=='') or (gender=='') or (age=='') or (occupation == ''):
            dlg = wx.MessageDialog(None, 'Some character details are missing. Be sure to fill out every box.', 'Missing Details', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False

        if db_program.dupCheck(name):
            dlg = wx.MessageDialog(None, 'This character is a duplicate. Please check the database and try again.', 'Duplicate Error', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False

        db_program.newCharacters(name,gender,age,occupation)
        self.charName.Clear()
        self.charGenF.SetValue(False)
        self.charGenM.SetValue(False)
        self.charAge.SetValue(0)
        self.charOcc.Clear()
        self.fillListCnt()

    def fillListCnt(self):
        self.listCnt.DeleteAllItems()
        allData = db_program.viewAll()
        for row in allData:
            self.listCnt.Append(row)

    def onDelete(self, event):
        db_program.deleteCharacter(self.selectedID)
        self.fillListCnt()
        dlg = wx.MessageDialog(None,'Character has been deleted.', 'Delete Complete', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def exitProgram(self, Event):
        self.Destroy()

app = wx.App()
frame = Frame('Python GUI')
frame.Show()

app.MainLoop()
