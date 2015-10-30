import choosers

class Player(object):
	def __init__(self, chooser):
		self.chooser = chooser
	def choice(self):
		return self.chooser.select_one()
	
	def take(self, chip):
		if self.chips[chip]:
			print('taken {c}'.format(c = chip))
			self.chips[chip] = False
			return True
		else:
			return False
		
	def check_chips(self):
		for x in self.chips:
			if x:
				return True
		return False
	
	def reset(self):
		self.chips = [True, True, True, True, True, True]
	def __str__(self):
		return 'Chips %s' % self.chips