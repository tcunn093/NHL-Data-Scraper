from lxml import html
import requests
from directoryref import HTMLReportDirectory

page = requests.get("http://www.nhl.com/ice/teams.htm")
tree = html.fromstring(page.text)

TeamPlaceList = tree.xpath('//span[@class="teamPlace"]/text()')
TeamCommonList = tree.xpath('//span[@class="teamCommon"]/text()')

TeamTuple = list(set(zip(TeamPlaceList, TeamCommonList)))
TeamList = []
for teams in TeamTuple:
	TeamList = [' '.join(teams) for teams in TeamTuple]

rawSrc = HTMLReportDirectory + "\\List of NHL Teams.txt"
wRawSrc = open(rawSrc, "w")

for team in sorted(TeamList):
	printinfo = "%s\n" % team
	wRawSrc.write(printinfo.encode('utf8'))

