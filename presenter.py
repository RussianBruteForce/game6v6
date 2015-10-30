from game import Game
from datetime import datetime
from statistics import Statistics
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
#from gui import MainWindow

class Presenter(QObject):
	endOfGame = pyqtSignal()
	scoreChangedTop = pyqtSignal(int)
	scoreChangedBot = pyqtSignal(int)
	disableChipTop = pyqtSignal(int)
	disableChipBot = pyqtSignal(int)
	statusChanged = pyqtSignal(str)
	
	def __init__(self, view):
		QObject.__init__(self)
		self.tie = True
		self.__view = view
		self.n = 6
		self.__stats = Statistics()
		self.__game = Game(self.__stats)
	
	@pyqtSlot(int)
	def chooseChip(self, chip):
		self.start(chip)
	
	#@pyqtSlot()
	def game_end(self):
		#if self.__game.stats[1] == self.__game.stats[0]:
		#	self.reset()
		#	return
		#winner = 0
		#looser = 1
		#if self.__game.stats[1] > self.__game.stats[0]:
		#	winner = 1
		#	looser = 0
		#self.__game.statisstic_logger.addGame(self.__game.players[winner], self.__game.players[looser],
		#			self.__game.stats[winner], self.__game.stats[looser],
		#			datetime.now().__str__());
		self.reset()
		#self.__view.exit()
	
	@pyqtSlot()
	def go(self):
		self.updateScore()
		self.start(666)
		
	@pyqtSlot()
	def start(self, p):
		if (p == 666):
			self.statusChanged.emit('Choose chip')
			return
		print('c start')
		
			
		status = str()
		
		print('take from p')
		self.__game.players[0].take(p)
		print('take from c')
		c = Game.ask_chip(self.__game.players[1])
		status += 'You choosed {pc} and PC choosed {cc}. '.format(pc = p+1, cc = c+1)
		
		#	else:
		#		self.new(self.__game.players[0].name)

		#self.print_chips()
		#print('\nYour chips:')
		#print(self.players[0])
		#p1 = Game.ask_chip(self.players[1])
		print('checking')
		if p < c:
			print('c win')
			#winner = self.players[1]
			status += 'So you lose!<br>'
			self.__game.stats[1] += p + c + 2
		elif p > c:
			print('p win')
			#winner = self.players[0]
			status += 'So you win!<br>'
			self.__game.stats[0] += p + c + 2
		else:
			print('tie')
			status += 'Tie!<br>'
			if self.__game.players[0].check_chips() == False:
				#self.tie = True
				self.reset()
				return
			print('give back')
			self.__game.give_back(p, c)
			status += 'Choose chip.'
			self.statusChanged.emit(status)
			return
		#print("Player {0} wins!\n".format(winner.name))
		self.disableChipTop.emit(c)
		self.disableChipBot.emit(p)
		status += 'Choose chip'
		self.statusChanged.emit(status)
		self.updateScore()
		
		if self.__game.players[0].check_chips() == False:
			print('no chips')
			if self.__game.end():
				#self.statusChanged.emit("Let's try more. Choose chip.")
				self.tie = False
				self.game_end()
				return
			else:
				self.reset()
		else:
			print(self.__game.players[0])
			print(self.__game.players[1])
	
	def winner_name(self):
		if self.__game.stats[1] > self.__game.stats[0]:
			return self.__game.players[1].name
		else:
			return self.__game.players[0].name
	
	def reset(self):
		if self.tie:
			status = "Let's try more. Choose chip."
		else:
			self.tie = True
			status = "Player {p} won last time.<br>This is new game. Choose chip.".format(p = self.winner_name())
			
		self.statusChanged.emit(status)
		self.__game.new()
		self.updateScore()
		self.__view.reset()
		#self.statusChanged.emit("LEL!")
		
	def updateScore(self):
		self.scoreChangedTop.emit(self.__game.stats[1])
		self.scoreChangedBot.emit(self.__game.stats[0])
	
	def nameTop(self):
		return self.__game.players[1].name
	
	def nameBot(self):
		return self.__game.players[0].name
