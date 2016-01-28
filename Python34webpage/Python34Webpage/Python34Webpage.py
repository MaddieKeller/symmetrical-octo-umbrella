import os, webbrowser
from tkinter import *
from tkinter import ttk

global outputHTML, htmlFile, bodyText
'''
   Objective: Create a webpage and a simple GUI to allow a user to edit the body text.
'''
def makeWindow():
    global bodyText
    win = Tk()
    win.title("Create a basic webpage")
    frame = Frame()
    Label(frame, text = "Enter the body text for the web page").pack()
    bodyText = Text(frame,height = 5, width = 100, wrap = WORD)
    submit = Button(frame, text = "Create Page", command = createHtml)
    
    bodyText.pack()
    submit.pack()
    frame.pack()

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

def main():  
    global outputHTML, htmlFile

    win = makeWindow()
    win.mainloop()



if __name__ == '__main__':main()