from tkinter import *
from tkinter import ttk
from tkinter import messagebox

global namebox
global emailbox
global survey

def submitButton():
    checkName(namebox.get())
    checkEmail(emailbox.get())
    checkSurvey(survey.get('1.0', 'end'))
    print('Name: {}'.format(namebox.get()))
    print('Email: {}'.format(emailbox.get()))
    print('Comments: {}'.format(survey.get('1.0','end')))

    clearButtion()

    messagebox.showinfo(title="Sucess",message = "Comments Successfully submitted.")

def clearButtion():
    namebox.delete(0, END)
    emailbox.delete(0, END)
    survey.delete('1.0', 'end')

def checkName(value):
    if value == '':
        messagebox.showerror(title = 'Entry Error',message = 'Please enter your name.')


def checkEmail(value):
    if value == '':
        messagebox.showerror(title = 'Entry Error', message = "Please enter a valid email address.")


def checkSurvey(value):
    if value == '':
        messagebox.showerror(title = 'Entry Error', message = 'Please leave a comment.')

class Feedback:
    def __init__(self, master):
        global namebox
        global emailbox
        global survey

        master.config(background = 'white')
        master.title("Feedback form")
        self.logo = PhotoImage(file = "C:\\Users\\Madison\\Downloads\\desert_desc_bug.gif")
        label = ttk.Label(master, text = "Please fill out the survey form below about your trip.")
        label.config(image = self.logo)
        label.config(compound = "left")
        label.config(background = 'white')
        label.grid(row = 0, column = 0, columnspan = 4)

        surveyFrame = Frame(master, padx = 5, background = 'white')

        namebox = Entry(surveyFrame)
        namelabel = ttk.Label(surveyFrame,text = "Enter Your Name: ", background = 'white')
        namelabel.grid(row = 0, column = 0)
        namebox.grid(row = 0, column = 1, sticky = 'ew')


        emailbox = Entry(surveyFrame)
        emaillabel = ttk.Label(surveyFrame, text = "Enter Your Email: ", background = 'white')
        emailbox.grid(row = 1, column = 1, sticky = 'ew')
        emaillabel.grid(row = 1, column = 0)

        surveylabel = ttk.Label(surveyFrame,text="Comments: ", background = 'white')
        survey = Text(surveyFrame, width = 50, height = 10, wrap = 'word')
        scrollbar = ttk.Scrollbar(surveyFrame, orient = VERTICAL, command = survey.yview)

        surveylabel.grid(row = 3,column = 0)
        survey.grid(row=3,column = 1,columnspan = 3)
        scrollbar.grid(row = 3, column = 4, sticky = 'ns')
        survey.config(yscrollcommand = scrollbar.set)

        surveyFrame.grid(row = 1, column = 0, columnspan = 4)

        submitBt = ttk.Button(master, text = "SUBMIT", command = submitButton)
        clearBt = ttk.Button(master, text = "CLEAR", command = clearButtion)
        submitBt.grid(row = 5, column = 1)
        clearBt.grid(row = 5, column = 2)

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == '__main__':main()