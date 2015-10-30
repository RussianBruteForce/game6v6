#!/usr/bin/python
import sys
import time
from chip_button import ChipButton
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from presenter import Presenter

class MainWindow(QWidget):
	ready = pyqtSignal()
	
	def __init__(self, pres = None):
		QWidget.__init__(self)
		if not pres:
			self.__presenter = Presenter(self);
		else:
			self.__presenter = pres;
		
		self.__n = self.__presenter.n
		
		scoreTop = QLabel('0')
		scoreBot = QLabel('0')
		
		self.__sT = scoreTop
		self.__sB = scoreBot
		
		self.buttons_top = list()
		self.buttons_bot = list()
		topL = QHBoxLayout()
		topL.addWidget(scoreTop)
		botL = QHBoxLayout()
		botL.addWidget(scoreBot)
		
		for x in range (0, self.__n):
			chip_weight = x + 1
			self.buttons_top.append(ChipButton(x, self))
			self.buttons_top[-1].setText("{i}".format(i = chip_weight))
			topL.addWidget(self.buttons_top[-1])
			self.buttons_bot.append(ChipButton(x, self))
			self.buttons_bot[-1].setText("{i}".format(i = chip_weight))
			botL.addWidget(self.buttons_bot[-1])
			self.buttons_bot[-1].chooseSignal.connect(self.__presenter.chooseChip)
		
		self.__centralLabel = QTextBrowser(self)
		
		#exitButton = QPushButton("Exit")
		
		mainLayout = QVBoxLayout()
		mainLayout.addLayout(topL)
		mainLayout.addWidget(self.__centralLabel)
		mainLayout.addLayout(botL)
		#mainLayout.addWidget(exitButton)
		self.setLayout(mainLayout)
		
		self.__presenter.statusChanged.connect(self.setStatus)
		self.__presenter.scoreChangedTop.connect(self.setScoreTop)
		self.__presenter.scoreChangedBot.connect(self.setScoreBot)
		self.__presenter.disableChipTop.connect(self.disableButtonTop)
		self.__presenter.disableChipBot.connect(self.disableButtonBot)
		self.ready.connect(self.__presenter.go)
		self.ready.emit()
	
	@pyqtSlot(str)
	def setStatus(self, status):
		self.__centralLabel.setText('<center>{text}</center>'.format(text=status))
	
	@pyqtSlot(int)
	def disableButtonTop(self, x):
		self.buttons_top[x].setEnabled(False)
		
	@pyqtSlot(int)
	def disableButtonBot(self, x):
		self.buttons_bot[x].setEnabled(False)
		
	@pyqtSlot(int)
	def setScoreTop(self, x):
		self.__sT.setText('{name} scrore: {score}'.format(score = x, name = self.__presenter.nameTop()))
		
	@pyqtSlot(int)
	def setScoreBot(self, x):
		self.__sB.setText('{name} scrore: {score}'.format(score = x, name = self.__presenter.nameBot()))

	def resizeEvent(self, event):
		event.accept()
	
	def exit(self):
		self.setEnabled(False)
		self.setStatus("")
		#time.sleep(5)
		#self.close()
		
	def reset(self):
		for x in range (0, self.__n):
			self.buttons_top[x].setEnabled(True)
			self.buttons_bot[x].setEnabled(True)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
