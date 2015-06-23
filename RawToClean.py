from directoryref import HTMLReportDirectory
import re
from StatArrays import *
import string

#Open the textfile and designate each line as an entry in a list
textlist = open(HTMLReportDirectory + "\\2003-2004\\20001.txt", "r").read().splitlines()

#Remove every instance in the list that is contained within "<" and ">"
textlist = filter(None,[re.sub('<[^>]+>', '', i) for i in textlist])

#Remove any instance in the list after '<!--', and also remove anything that contains only empty space 
textlist = [x for x in textlist if textlist.index(x) < textlist.index('<!--') and not x.isspace()]

#Find hyphenLine in textfile and convert it to a single string
hyphenLine = "".join([x for x in textlist if not x.find('-') ])

#Count the spaces up to the next column and append the number of spaces to a list
columnwidths = []
for i in range(len(hyphenLine) - 1):
 	if hyphenLine[i] + hyphenLine[i+1] == " -":
 		columnwidths.append(i+1)

columnwidths = [0] + columnwidths

copyrightLineIndex = textlist.index("".join([x for x in textlist if "Copyright" in x ]))
hyphenLineIndex = textlist.index(hyphenLine)

def indexOfFirstCharacter(s):
	return len(s) - len(s.lstrip())

def listFill(List, thing):
	for _ in range(hyphenLineIndex, copyrightLineIndex):
		List.append(thing)
	return List

def removePunctuation(s):
	return re.sub(r'[^\w\s]','',s)

def splitString(s):
	return s.split()

def refunref(i, b):
	if b == True:
		i = i - hyphenLineIndex
	else:
		i = i + hyphenLineIndex 
	return i

def returnNumbers(s):
	numbers = map(int, re.findall('\d+', removePunctuation(s)))
	return tuple(numbers)

def returnPlusMinusNames(s):
	List = removePunctuation(s).split()
	List = [x for x in List if not re.search('\d+', x)]
	List.pop(0)
	return tuple(List)
	
def returnPlusMinusTeam(s):
	return removePunctuation(s.split()[0])


def addPlus(s, i, k):
	PlusPlayerNumbers[i] = returnNumbers(s)
	PlusPlayerNames[i] = returnPlusMinusNames(s)
	PlusTeam[i] = returnPlusMinusTeam(s)

def addMinus(s, i, k):
	MinusPlayerNumbers[i] = returnNumbers(s)
	MinusPlayerNames[i] = returnPlusMinusNames(s)
	MinusTeam[i] = returnPlusMinusTeam(s)

def getUniqueList(List):
	return set(List)

def addEventData(i,eventType):

	description = removePunctuation(textlist[i][-(len(textlist[i]) - columnwidths[-1]):])

	k = refunref(i,True) - 1

	if "GOAL" in eventType:

		numbers = [x for x in description.split() if x.isdigit() == True]
		ScorerNumber[k] = description.split()[0]
		ScorerName[k] = description.split()[1]
		if len(numbers) > 2:
			FirstAssistNumber[k] = numbers[1]
			FirstAssistName[k] = description.split()[4]
		if len(numbers) > 3:
			SecondAssistNumber[k] = numbers[2]
			SecondAssistName[k] = description.split()[7]
		GoalShotType[k] = description.split()[-2]
		GoalShotLength[k] = numbers[-1]
		
		
	if "FACE-OFF" in eventType:

		numbers = [x for x in description.split() if x.isdigit() == True]
		FaceOffWinnerTeam[k] = description.split()[0]
		FaceOffLocation[k]= description.split()[2]
		FaceOffWinnerNumber[k] = numbers[0]
		FaceOffWinnerName[k] = description.split()[6]
		FaceOffLoserNumber[k] = numbers[1]
		FaceOffLoserName[k] = description.split()[-1]


	if "SHOT (*)" in eventType:

	#if eventType == "SHOT":

	#if eventType == "STOPPAGE":

	#if eventType == "SHOT (!)":

	#if eventType == "PENALTY":


for i in nonConstantsInt:
	for j in i:
		listFill(j, "")

for i in nonConstantsTup:
	for j in i:
		listFill(j, ())

b = 2
d = 0

for i in range(hyphenLineIndex + 1, copyrightLineIndex):

	if indexOfFirstCharacter(textlist[i]) <= 4:

		for j in range(len(RawData)):

			RawData[j].append(textlist[i][columnwidths[j]:columnwidths[j+1]])

		
		
		addEventData(i, Event[refunref(i,True)-1 - (b-2)])

	else:

		d= i - 1
		d = refunref(d, True)
		k =  refunref(i, True)

		if b % 2 == 0:

			addPlus(textlist[refunref(k, False)], (d-1) - (b - 2), k)

		else:

			addMinus(textlist[refunref(k, False)], (d-1) - (b - 2), k)
		
		b += 1


for i in textlist:
	print i

