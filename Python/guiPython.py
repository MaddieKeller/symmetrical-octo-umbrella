import wx

class Frame(wx.Frame):
    def __init__(self, parent, title):  #create an initialize function

        wx.Frame.__init__(self, parent, title=title, pos=(0,0))  #parent and title are variables passed in from the function
        #self.Center()  #centers the window
        #self.Move((600,400))#moves window to (x,y) position on screen
        self.Maximize()

        panel = wx.Panel(self)  #add a panel that we can add text and buttons to

        button = wx.Button(panel, \
                           label="Exit", \
                           size=(90,40), \
                           pos=(100,70))  #add the button
        button.Bind(wx.EVT_BUTTON, \
                    self.exit)  #bind the button to an exit event
        menuBar = wx.MenuBar()  #create a menu bar
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        #add the menu items to the menu
        menuBar.Append(fileMenu, 'File')
        menuBar.Append(editMenu, 'Edit')

        #Add items to the menu items
        fileMenu.Append(wx.NewId(), \
                        'New File', \
                        'Create a New File')
        fileMenu.Append(wx.NewId(), \
                        'Open', \
                        'Open a Saved File')
        editMenu.Append(wx.NewId(), \
                        'Edit File', \
                        'Edit a Previously Created File')

        exitItem = fileMenu.Append(wx.NewId(), \
                                   'Exit', \
                                   'Exit the Program')  #create exit menu item and assign to exitItem
        self.Bind(wx.EVT_MENU, \
                  self.exit, \
                  exitItem)  #bind exit function to exitItem


        self.SetMenuBar(menuBar)  #Add the menu bar to the window
        self.CreateStatusBar()  #Add a status bar to the window

        wx.StaticText(panel, \
                      label="This is a Python GUI window.", \
                      pos=(10,10))  #This is a static line of text

        wx.StaticBox(panel, label="A collection of stuff",pos=(20,30),size=(200,100))  #a static box outline with title
        wx.StaticText(panel, label="Text inside a box", pos=(30,50))  #static text positioned inside a box

        comboText = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        combo = wx.ComboBox(panel, pos=(280,30), choices=comboText)

        #checkbox section
        wx.StaticBox(panel, label="Color:", size=(100,120), pos=(390,0))
        wx.CheckBox(panel, label="Green", pos=(400,30))
        wx.CheckBox(panel, label="Black", pos=(400,60))
        wx.CheckBox(panel, label="Blue", pos=(400,90))

        #radio buttons
        wx.StaticBox(panel, label="Sex:", size=(100,120), pos=(490,0))
        wx.RadioButton(panel, label="Male", pos=(500,30))
        wx.RadioButton(panel, label="Female", pos=(500,60))
        wx.RadioButton(panel, label="Other", pos=(500,90))

        wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300,100), pos=(600,10))

        #spin control that controls some text
        self.sc = wx.SpinCtrl(panel, value="0", size=(70,25), pos=(300,150))  #create spin control
        self.valueText = wx.StaticText(panel, label="Hello", pos=(300,200))  #create text box
        self.sc.Bind(wx.EVT_SPINCTRL, self.spinControl)  #bind control to function


    def spinControl(self, Event):  #function for Spin Control to change text value
        value = self.sc.GetValue()  #get current value of spin control
        self.valueText.SetLabel(str(value))  #change the label of the text box to the number of the spin control

    def exit(self, Event):  #create an exit function
        self.Destroy()


app = wx.App()

frame = Frame(None, "Python GUI")  #pass in the parent and title
frame.Show()
app.MainLoop()


