import sqlite3

database_location = 'lyrics.db'

class database():
	def __init__():
		self.c = sqlite3.connect(database_location)
		
	def addSong(self, title, lyrics, copyright=''):
		t = (title, lyrics, copyright)
		self.c.execute('INSERT INTO songs VALUES (auto, ?,?,?)', t)
		self.c.commit()
		
	def removeSong(self, id):
		print "blah"
		
	def fetchSong(self, id):
		t = (id, )
		self.c.execute('select * from songs where id = ?', t)
		return list(c)
		
	def searchSongs(self, text):
		t = (text,)
		self.c.execute('select * from songs where title or lyrics = ?', t)
		
		return list(c)
		
	
