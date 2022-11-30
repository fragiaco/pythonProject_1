

from tkinter import *

class Myapp:
    def __init__(self, master):
        self.master = master
        self.master.title('semplice GUI')
        self.master.geometry('600x400')
        self.label = Label (master,text='LABEL')
        self.label.pack()
        self.button = Button (master,text='click me',command=self.btn_action())
        self.button.pack()

    def btn_action(self):
            pass

window = Tk()



mywindow = Myapp(window)
window.mainloop()




