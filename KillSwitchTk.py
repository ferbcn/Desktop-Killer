"""
Desktop Icon Hide Button
Implemented in Python
GUI (Tkinter)
Author: ferbcn
TO-DO: Win & Linux
"""

import sys
import os
from tkinter import *
import platform

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.icons_hidden = False


    def hide_desktop(self):
        if not self.icons_hidden:
            print('Hiding Desktop Icons')
            os.system('defaults write com.apple.finder CreateDesktop false')
            self.icons_hidden = True
            self.killer.config(text='UNHIDE')
            #self.button.setStyleSheet("background-color: darkgrey")
        else:
            print('Showing Desktop Icons')
            os.system('defaults write com.apple.finder CreateDesktop true')
            self.icons_hidden = False
            self.killer.config(text='HIDE')
            #self.button.setText('HIDE')
            #self.button.setStyleSheet("background-color: lightgrey")
        os.system('killall Finder')

    def createWidgets(self):
        #self.killer = Button(self, text='HIDE', bg='#0052cc', fg='#ffffff', command='self.hide_desktop')
        self.killer = Button(self, text="HIDE", command=self.hide_desktop, width=30, height=30)
        self.killer.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("Desktop Icon Kill Switch")
    root.geometry("100x100")
    app = Application(master=root)
    app.mainloop()
    #root.destroy()