import urllib2
from urllib2 import HTTPError
from urllib2 import urlopen
from cookielib import CookieJar
from datetime import date
import re
import os

#Number of games in NHL Season: 1230
#First year that NHL.com released HTML Reports: 2003-2004
year = str(20032004)
gamenumber = str(20001)

def numberofcycles(year):
	return int(date.today().year) - int(year[:4])

def incyear(year):
	year = int(year)
	year = year + 10001
	return str(year)

def incgamenum(gamenumber):
	gamenumber = int(gamenumber)
	if gamenumber<21230:
		gamenumber += 1
	else:
		gamenumber = 20001

	return str(gamenumber)


def nhlhtmlsheeturl(year, gamenumber):
	url = "http://www.nhl.com/scores/htmlreports/" + year + "/PL0" + gamenumber + ".HTM"
	return url

def createfile(yeardirectory):
	
	if not os.path.exists(yeardirectory):
    		os.makedirs(yeardirectory)

def yearwithhyphen(year):
	year = year[:4] + "-" + year[-4:]
	return year

def sourcecodetotext(url, gamenumber, year):

	try:
		webPage=urllib2.urlopen(url)
		rawSrc = makestringpath(yearwithhyphen(year)) + "\\" + gamenumber + ".txt"
		wRawSrc = open(rawSrc, "w")
		wPageSrc=webPage.read()
		webPage.close()
		wRawSrc.write(wPageSrc)

	except HTTPError:
		print "Game %s in year %s does not exist in HTML Report database" %(gamenumber, year)

def makestringpath(year):
	directory = 'C:\\Users\\Owner\\Desktop\\NHL HTML Reports\\' + year
	return directory


for _ in range(1230*numberofcycles(year)):

	url = nhlhtmlsheeturl(year, gamenumber)
	sourcecodetotext(url, gamenumber, year)
	print gamenumber
	gamenumber = incgamenum(gamenumber)

	if int(gamenumber) == 20001:
		year = incyear(year)
		createfile(makestringpath(yearwithhyphen(year)))
		print yearwithhyphen(year)
