from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class ChipButton(QPushButton):
	chooseSignal = pyqtSignal(int)

	def __init__(self, id, parent = None):
		super(ChipButton, self).__init__(parent)
		self.id = id
		self.clicked.connect(self.choose)
	
	@pyqtSlot()
	def choose(self):
		self.chooseSignal.emit(self.id)
	