import os, webbrowser
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import db_connect


global outputHTML, htmlFile, bodyText
'''
   Objective: Create a webpage and a simple GUI to allow a user to edit the body text.
'''
def makeWindow():
    global bodyText
    win = Tk()
    win.title("Create a basic webpage")
    frame = Frame()

    #setup the text entry
    label = Label(frame, text = "Enter the body text for the web page").grid(row = 0, column = 0, columnspan = 5, sticky = 'nsew')
    bodyText = Text(frame, wrap = WORD)
    bodyScroll = Scrollbar(frame,orient = VERTICAL)
    bodyText.config(yscrollcommand = bodyScroll.set)
    bodyScroll['command']=bodyText.yview()
    submit = Button(frame, text = "Create Page", command = createHtml)
    
    bodyText.grid(row = 1, column = 0, columnspan = 4, sticky = 'nsew')
    bodyScroll.grid(row = 1, column = 4, sticky = 'nsew')
    submit.grid(row = 2, column = 1)
    frame.pack(expand = True, fill = 'both')
    frame.grid_rowconfigure(0, weight = 1)
    frame.grid_columnconfigure(0, weight = 1) 
   
    listBox = MultiColumnListbox()
    return win

def createHtml():
    global outputHTML, htmlFile
    userInput = bodyText.get(1.0,END)
    currentPath = os.path.dirname(os.path.abspath(__file__))
    outputHTML = currentPath + '/sale.html'

    htmlFile = open(outputHTML,"w")
    html =    ('''<html>
    <body> {}
    </body>
    </html>'''.format(userInput))
    htmlFile.write(html)
    htmlFile.close()
    webbrowser.open(outputHTML)

class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def callback(self, event):
        selectLine = self.tree.item(self.tree.selection())
        selection = selectLine['values']
        bodyText.delete(1.0,END)
        print(selection[2])
        bodyText.insert(1.0,selection[2])

    def _setup_widgets(self):
        s = """\click on header to sort by that column to change width of column drag boundary"""
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
          padding=(10, 2, 10, 6), text=s)
        msg.pack(fill='x')
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=content_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)

        self.tree.bind('<<TreeviewSelect>>', self.callback)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        
        for col in content_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in content_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(content_header[ix],width=None)<col_w:
                    self.tree.column(content_header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))



def main():  
    global outputHTML, htmlFile

    win = makeWindow()
    win.mainloop()

content_header = ("ID","Description","Content")
content_list = db_connect.getContent()


if __name__ == '__main__':main()