import json
import operator
import sys

class Statistics(object):
	def __init__(self):
		self.db = []
		self.filename = 'stats.json'
		self.cached = False
		self.new = True
		try:
			f = open(self.filename, 'r')
			print ('Finded old stats')
			self.db = json.loads(f.read())
			f.close()
			self.new = False
			print('readed {s} games'.format(s = len(self.db)))
		except FileNotFoundError:
			print ("No stats file {file} found. Will create later.".format(file=self.filename))
			#sys.exit(-1)
	
	def addGame(self, winner, loser, winner_score, looser_score, time):
		print('adding at list size {s}'.format(s = len(self.db)))
		self.db.append({"time" : time,
			"winner" : {
				"name" : winner.name,
				"score" : winner_score
				},
			"looser" : {
				"name" : loser.name,
				"score" : looser_score
			}
		})
		self.write_file()
		self.cached = False
	
	def write_file(self):
		f = open(self.filename, 'w')
		#print('writing file')
		f.write( json.dumps(self.db, sort_keys=False, indent=4) )
		f.close
		
	def read_file(self):
		if not self.new:
			try:
				f = open(self.filename, 'r')
			except FileNotFoundError:
				print ("Can't open {file}".format(file=self.filename))
				sys.exit(-1)
		#print ("Loaded: ", json.loads(f.read()))
			self.db = json.loads(f.read())
		#print(self.db[0]['time'])
			f.close()
		#print('readed {s} games'.format(s = len(self.db)))
			self.cached = False
		else:
			print ('nothing to read')
		
	def __gen_rating(self):
		self.rating = dict()
		for g in self.db:
			name = g['winner']['name']
			if name in self.rating:
				self.rating[name] += 1
			else:
				self.rating[name] = 1
			name = g['looser']['name']
			if name not in self.rating:
				self.rating[name] = 0
		self.cached = True
	
	def top_player(self):
		if not self.cached:
			self.__gen_rating()
		return sorted(self.rating.items(), key=operator.itemgetter(1))[-1]
	
	def players(self):
		if not self.cached:
			self.__gen_rating()
		players = list()
		for p in self.rating:
			players.append(p)
		return sorted(players, key=str.lower)
	
	def log(self):
		if not self.cached:
			self.__gen_rating()
		return self.db
	
	def games_played(self):
		return len(self.db)
	