from game_players import *
import choosers
import os
from datetime import datetime

class Game(object):
	def __init__(self, statisstic_logger, player_name = 'Anon'):
		self.new(player_name)
		self.statisstic_logger = statisstic_logger
	
	def new(self, player_name = 'Anon'):
		self.players = [Man(player_name, choosers.StdinChooser(0,5)),
			        Comp(choosers.MyChooser(0,5))]
		self.stats = [0, 0]
	
	def print_chips(self):
		print('{2}:\t{0}\n{3}:\t{1}'.format(self.players[0], self.players[1],
						    self.players[0].name, self.players[1].name))

	def ask_chip(player):
		while True:
			p = player.choice()
			#print(p)
			if p == 666:
				return p;
			if player.take(p):
				break
		return p

	def give_back(self, p0, p1):
		self.players[0].chips[p0] = True
		self.players[1].chips[p1] = True

	def end(self):
		winner = 0
		looser = 1
		
		if self.stats[1] > self.stats[0]:
			winner = 1
			looser = 0
		elif self.stats[1] == self.stats[0]:
			return False
		print("Player {0} takes all!\n".format(self.players[winner].name))
		self.statisstic_logger.addGame(self.players[winner], self.players[looser],
				 self.stats[winner], self.stats[looser],
				 datetime.now().__str__());
		return True

	def __str__(self):
		return "\n*** Score ***\n {0}:\t{1}\n{2}:\t{3}".format(self.players[0].name, self.stats[0],
						       self.players[1].name, self.stats[1])

	def start(self):
		print('*** {0} vs. {1} ***'.format(self.players[0].name, self.players[1].name))
		self.print_chips()
		while True:
			#os.system('clear')
			print(self)
			if self.players[0].check_chips() == False:
				if self.end():
					return
				else:
					self.new(self.players[0].name)
			
			self.print_chips()
			#print('\nYour chips:')
			#print(self.players[0])
			p0 = Game.ask_chip(self.players[0])
			if p0 == 666:
				self.statisstic_logger.write_file()
				print('bye!')
				return 1
			p1 = Game.ask_chip(self.players[1])
			if p0 < p1:
				winner = self.players[1]
				self.stats[1] += p0 + p1 + 2
			elif p0 > p1:
				winner = self.players[0]
				self.stats[0] += p0 + p1 + 2
			else:
				print("Draw\n")
				if self.players[0].check_chips() == False:
					self.end()
					return
				self.give_back(p0, p1)
				continue
			print("Player {0} wins!\n".format(winner.name))