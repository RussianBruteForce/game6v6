#!/usr/bin/python
from game import Game
import time
from statistics import Statistics

stats = Statistics()
g = Game(stats)

if __name__ == '__main__':
	while True:
		g.start()
		time.sleep(5)
		g.new()