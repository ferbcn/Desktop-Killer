import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class PushButton (QWidget):

    def __init__ (self):
        super ().__init__ ()
        self.title = 'Desktop Icons Kill Switch'
        self.width = 200
        self.height = 140
        self.left = 10
        self.top = 10
        self.initUI ()
        self.icons_hidden = False

    def initUI (self):
        self.setWindowTitle (self.title)
        self.setGeometry (self.left, self.top, self.width, self.height)

        self.button = QPushButton ('HIDE', self)
        self.button.setToolTip ('Hide / Unhide Desktop Icons')
        self.button.setStyleSheet ("background-color: lightgrey")
        self.button.move (10, 20)
        self. button.setMinimumHeight(100)
        self.button.setMinimumWidth(180)
        self.button.clicked.connect (self.on_click)

        self.show ()

    @pyqtSlot ()
    def on_click (self):
        if not self.icons_hidden:
            print ('Hiding Desktop Icons')
            os.system('defaults write com.apple.finder CreateDesktop false')
            self.icons_hidden = True
            self.button.setText('UNHIDE')
            self.button.setStyleSheet ("background-color: darkgrey")
        else:
            print ('Showing Desktop Icons')
            os.system ('defaults write com.apple.finder CreateDesktop true')
            self.icons_hidden = False
            self.button.setText ('HIDE')
            self.button.setStyleSheet ("background-color: lightgrey")
        os.system('killall Finder')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    button = PushButton()
    sys.exit(app.exec_())

"""
defaults write com.apple.finder CreateDesktop false, killall Finder
"""