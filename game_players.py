import player

class Man(player.Player):
	def __init__(self, name, chooser):
		player.Player.__init__(self, chooser)
		self.name = name
		self.reset()

class Comp(player.Player):
	def __init__(self, chooser):
		player.Player.__init__(self, chooser)
		self.name = 'PC'
		self.reset()