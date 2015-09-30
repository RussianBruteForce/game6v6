#!/usr/bin/python
import sys
import statistics
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.stats = statistics.Statistics()
		
		tabs = QTabWidget()
		
		stats_widget = QWidget()
		stats_layout = QGridLayout(stats_widget)
		self.top_player_l = QLabel()
		self.games_played_l = QLabel()
		self.players_l = QLabel()
		stats_layout.addWidget(self.top_player_l, 0,0)
		stats_layout.addWidget(self.games_played_l, 1,0)
		stats_layout.addWidget(self.players_l, 2,0)
		
		update_button = QPushButton('Update stats')
		stats_layout.addWidget(update_button, 3,0)
		
		log_widget = QWidget()
		log_layout = QHBoxLayout(log_widget)
		self.log_browser = QTextBrowser()
		log_layout.addWidget(self.log_browser)
		
		tabs.addTab(stats_widget, "Stats")
		tabs.addTab(log_widget, "Log")
		
		update_button.clicked.connect(self.update)
		
		self.setCentralWidget(tabs)
		self.resize(400, 240)
		self.update()
	
	def update(self):
		self.stats.read_file()
		top_player = self.stats.top_player()
		games_played = self.stats.games_played()
		players =  '<br>'.join(self.stats.players())
		#print(self.stats.players())
		
		self.top_player_l.setText(str('Top player is <b>{name}</b> with {wins} wins!').format(name=top_player[0], wins=top_player[1]))
		self.games_played_l.setText('Games logged: {num}'.format(num=games_played))
		self.players_l.setText('<b>Players:</b> <br><center>{list}</center>'.format(list=players))
		
		db = self.stats.log()
		log = str()
		for g in db:
			line = '&lt;{time}&gt; <font color="green">{wname}</font> vs. <font color="red">{lname}</font>  = <b>{wscore}:{lscore}</b><br>'.format(
				time = g['time'],
				wname = g['winner']['name'], wscore = g['winner']['score'],
				lname = g['looser']['name'], lscore = g['looser']['score'])
			log = log + line
		self.log_browser.setText(log)
		
	
	def resizeEvent(self, event):
		event.accept()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())