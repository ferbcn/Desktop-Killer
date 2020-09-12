"""
Desktop Icon Hide Button
Implemented in Python
GUI (Tkinter)
Author: ferbcn
"""

# import sys
import os
from tkinter import *
import platform

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.icons_hidden = False
        self.os = platform.system() # Darwin, Linux, Windows


    def createWidgets(self):
        self.killer = Button(self, text="HIDE", command=self.hide_desktop, width=30, height=30, fg='Red')
        self.killer.pack()


    def hide_desktop(self):
        if not self.icons_hidden:
            if self.os == "Darwin":
                os.system('defaults write com.apple.finder CreateDesktop false')
            elif self.os == "Linux":
                os.system('gsettings set org.gnome.desktop.background show-desktop-icons True')
            elif self.os == "Windows":
                pass
            else:
                print('Sorry, OS not supported!')
            print('Hiding Desktop Icons')
            self.icons_hidden = True
            self.killer.config(text='UNHIDE', fg='Green')
        else:
            print('Showing Desktop Icons')
            if self.os == "Darwin":
                os.system('defaults write com.apple.finder CreateDesktop true')
            elif self.os == "Linux":
                os.system('gsettings set org.gnome.desktop.background show-desktop-icons True')
            elif self.os == "Windows":
                pass
            else:
                print('Sorry, OS not supported!')
            self.icons_hidden = False
            self.killer.config(text='HIDE', fg='Red')
        os.system('killall Finder')


if __name__ == '__main__':
    root = Tk()
    root.title("Desktop Icon Kill Switch")
    root.geometry("100x100")
    app = Application(master=root)
    app.mainloop()
    #root.destroy()