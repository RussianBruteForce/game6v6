#!/usr/bin/python
from game import Game
import time
from statistics import Statistics
import sys

stats = Statistics()
g = Game(stats)

if __name__ == '__main__':
	while True:
		if g.start() == 1:
			sys.exit(1)
		time.sleep(5)
		g.new()
		#stats.read_file()