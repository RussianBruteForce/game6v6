#!/usr/bin/python
import sys
import statistics
from PyQt5.QtWidgets import *
from presenter import Presenter

class MainWindow(QWidget):
    def __init__(self):
	self.__n = 6
	QWidget.__init__(self)
	self.__presenter = Presenter(self);
	self.buttons_top = list()
	self.buttons_bot = list()
	topL = QHBoxLayout()
	botL = QHBoxLayout()
	for x in range (0, self.__n):
	    self.buttons_top.append(QPushButton())
	    self.buttons_top[-1].setText("{i}".format(i = x))
	    topL.addWidget(self.buttons_top[-1])
	    self.buttons_bot.append(QPushButton())
	    self.buttons_bot[-1].setText("{i}".format(i = x))
	    botL.addWidget(self.buttons_bot[-1])
	    mainLayout = QVBoxLayout()
	    mainLayout.addLayout(topL)
	    mainLayout.addLayout(botL)
	    setLayout(mainLayout)
    def resizeEvent(self, event):
	event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
