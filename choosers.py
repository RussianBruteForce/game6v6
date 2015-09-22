import random

class Chooser(object):
	def __init__(self, min_, max_):
		self.min_ = min_
		self.max_ = max_
	def select_one(self):
		pass

class RandomChooser(Chooser):
	def __init__(self, min_, max_):
		Chooser.__init__(self, min_, max_)
	def select_one(self):
		return random.randint(self.min_, self.max_)

class MyChooser(Chooser):
	def __init__(self, min_, max_):
		self.last = random.randint(min_, 2)
		Chooser.__init__(self, min_, max_)
	def select_one(self):
		a = self.last + random.randint(0, 3)
		if (a <= self.max_):
			self.last = a
			return a
		else:
			self.last = random.randint(self.min_ - 1, self.max_ - 2)
			return self.select_one()

class StdinChooser(Chooser):
	def __init__(self, min_, max_):
		Chooser.__init__(self, min_, max_)
		
	def switch_case(self,case):
		if case == 'q':
			return 1
		elif case == 'w':
			return 2
		elif case == 'e':
			return 3
		elif case == 'r':
			return 4
		elif case == 't':
			return 5
		elif case == 'y':
			return 6
		return case
	
	def select_one(self):
		ch = self.min_
		while ch < self.min_ + 1 or ch > self.max_ + 1:
			
			ch = input('Enter num from {0} to {1}:>'.format(self.min_ + 1,
						   self.max_ + 1))
			ch = self.switch_case(ch)
			try:
				ch = int(ch)
			except ValueError:
				return self.select_one()
		return ch - 1		