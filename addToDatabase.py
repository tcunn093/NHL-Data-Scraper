import sqlite3
from directoryref import HTMLReportDirectory
from RawToClean import GameNumber
conn = sqlite3.connect(HTMLReportDirectory + "NHLSQLITEDATABASE.db")

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS NHLData;')

c.execute('''CREATE TABLE NHLData
 (Season text, Game "#" text, Eventindex text, Period text, Time of Event text, Event text, Team Responsible text, Type text);''')

for j in range(len(Event)):
	c.execute("INSERT INTO NHLData VALUES(?,?,?,?,?,?,?,?);", 
	Season[j], 
	GameNumber[j], 
	EventIndex[j], 
	Period[j], 
	TimeOfEvent[j], 
	Event[j], 
	TeamResponsible[j], 
	Type[j])
	
