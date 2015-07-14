from directoryref import HTMLReportDirectory
import re
from StatArrays import *
import sqlite3

def indexOfFirstCharacter(s):
	return len(s) - len(s.lstrip())

def listFill(List, thing):
	for _ in range(hyphenLineIndex, lastLineIndex):
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

def indexfirstInstanceOf(s, List):
	i = 0
	while not s in List[i] and i < len(List) - 1:
		i = i+1
	if i == len(List) - 1:
		i = 0
	return i

def returnNumbers(s,i):

	numbers = [x for x in s.split() if x.isdigit() == True]
	# print i
	# print numbers
	return numbers[i]

def returnNames(s,i):
	List = removePunctuation(s).split()
	List = [x for x in List if not re.search('\d+', x)]
	List.pop(0)
	return List[i]
	
def returnPlusMinusTeam(s):
	return removePunctuation(s.split()[0])


def addPlus(s, i):
	#print i
	PlusPlayerOneNumber[i] = returnNumbers(s,0)
	PlusPlayerOneName[i] = returnNames(s,0)
	PlusTeam[i] = returnPlusMinusTeam(s)

	if len(s.split()) > 3:

		PlusPlayerTwoNumber[i] = returnNumbers(s,1)
		PlusPlayerTwoName[i] = returnNames(s,1)
		PlusPlayerThreeNumber[i] = returnNumbers(s,2)
		PlusPlayerThreeName[i] = returnNames(s,2)
		PlusPlayerFourNumber[i] = returnNumbers(s,3)
		PlusPlayerFourName[i] = returnNames(s,3)
		if len([x for x in s.split() if x.isdigit() == True]) == 6:
			PlusPlayerFiveNumber[i] = returnNumbers(s,4)
			PlusPlayerFiveName[i] = returnNames(s,4)
		if len([x for x in s.split() if x.isdigit() == True]) == 7:
			PlusPlayerSixNumber[i] = returnNumbers(s,5)
			PlusPlayerSixName[i] = returnNames(s,5)

def addMinus(s, i):

	MinusPlayerOneNumber[i] = returnNumbers(s,0)
	MinusPlayerOneName[i] = returnNames(s,0)
	MinusTeam[i] = returnPlusMinusTeam(s)

	if len(s.split()) > 3:
		MinusPlayerTwoNumber[i] = returnNumbers(s,1)
		MinusPlayerTwoName[i] = returnNames(s,1)
		MinusPlayerThreeNumber[i] = returnNumbers(s,2)
		MinusPlayerThreeName[i] = returnNames(s,2)
		MinusPlayerFourNumber[i] = returnNumbers(s,3)
		MinusPlayerFourName[i] = returnNames(s,3)
		if len([x for x in s.split() if x.isdigit() == True]) == 6:
			MinusPlayerFiveNumber[i] = returnNumbers(s,4)
			MinusPlayerFiveName[i] = returnNames(s,4)
		if len([x for x in s.split() if x.isdigit() == True]) == 7:
			MinusPlayerSixNumber[i] = returnNumbers(s,5)
			MinusPlayerSixName[i] = returnNames(s,5)

def getUniqueList(List):
	return set(List)

def addEventData(i,eventType):
	description = removePunctuation(textlist[i][-(len(textlist[i]) - columnwidths[-1]):])

	k = refunref(i,True) - 1 - (b-2)

	if "GOAL" in eventType:

		numbers = [x for x in description.split() if x.isdigit() == True]
		ScorerNumber[k] = description.split()[0]
		ScorerName[k] = description.split()[1]
		if len(numbers) > 2:
			FirstAssistNumber[k] = numbers[1]
			FirstAssistName[k] = description.split()[4]
		if len(numbers) > 3:
			SecondAssistNumber[k] = numbers[2]
			SecondAssistName[k] = description.split()[6]
		if len(numbers) <=2:
			GoalShotType[k] = description.split()[-3]
			GoalShotLength[k] = numbers[-1]
		
		
	if "FACE-OFF" in eventType:

		numbers = [x for x in description.split() if x.isdigit() == True]
		FaceOffWinnerTeam[k] = description.split()[0]
		FaceOffLocation[k]= description.split()[2]
		FaceOffWinnerNumber[k] = numbers[0]
		FaceOffWinnerName[k] = description.split()[6]
		FaceOffLoserNumber[k] = numbers[1]
		FaceOffLoserName[k] = description.split()[-1]


	if "SHOT" in eventType:
		ShooterNumber[k] = description.split()[0]
		ShooterName[k] = description.split()[1]
		ShotType[k] = description.split()[2]
		ShotDistance[k] = description.split()[3]


	if "STOPPAGE" in eventType:
		StoppageReason[k] = description

	if "PENALTY" in eventType:
		OffenderNumber[k] = description.split()[0]
		OffenderName[k] = description.split()[1]
		OffenceType[k] = description.split()[2]
		PenaltyLength[k] = description.split()[-1]


for q in range(20001, 21231):
	GameNumberString = str(q)
	print GameNumberString
	SeasonString = "2003-2004"

	textlist = open(HTMLReportDirectory + "\\" + SeasonString + "\\" + GameNumberString + ".txt", "r").read().splitlines()

	#Remove every instance in the list that is contained within "<" and ">"
	textlist = filter(None,[re.sub('<[^>]+>', '', i) for i in textlist])

	#Remove any instance in the list after '<!--', and also remove anything that contains only empty space 
	textlist = [x for x in textlist if not x.isspace()]

	if indexfirstInstanceOf("<!--", textlist) <> 0:
		textlist = [x for x in textlist if textlist.index(x) < textlist.index('<!--')]

	#Find hyphenLine in textfile and convert it to a single string
	hyphenLine = "".join([x for x in textlist if not x.find('-') ])

	#Count the number of characters between each instance of " -" to find the correct column width of each data column
	columnwidths = [0] + [i+1 for i in range(len(hyphenLine)-1) if hyphenLine[i] + hyphenLine[i+1] == " -" ]

	if "".join([x for x in textlist if "Copyright" in x ]) <> "":

		lastLineIndex = textlist.index("".join([x for x in textlist if "Copyright" in x ]))

	else: 
		lastLineIndex = len(textlist)



	hyphenLineIndex = textlist.index(hyphenLine)

	# for i in textlist:
	# 	print i

	for i in Description:
		for j in i:
			del j[:]
			listFill(j, "")

	for l in RawData:
		del l[:]

	for l in test:
		del l[:]

	listFill(Season, SeasonString)
	listFill(GameNumber, GameNumberString)

	b = 2
	d = 0

	for i in range(hyphenLineIndex + 1, lastLineIndex):

		if indexOfFirstCharacter(textlist[i]) <= 4:

			for j in range(len(RawData)):

				RawData[j].append(textlist[i][columnwidths[j]:columnwidths[j+1]].replace(" ",""))

			addEventData(i, Event[refunref(i,True)-1 - (b-2)])

		else:

			d = refunref(i-1, True)
			k =  refunref(i, True)

			if b % 2 == 0:
				
				addPlus(textlist[refunref(k, False)], (d-1) - (b - 2))

			else:

				addMinus(textlist[refunref(k, False)], (d-1) - (b - 2))
			
			b += 1



	conn = sqlite3.connect(HTMLReportDirectory + "NHLSQLITEDATABASE.db")

	c = conn.cursor()
	if GameNumberString == "20001":

		c.execute('DROP TABLE IF EXISTS NHLData;')

		c.execute('''CREATE TABLE NHLData
		 (Season text, 
		 GameNumber text, 
		 EventIndex text, 
		 Period text, 
		 TimeOfEvent text, 
		 Event text, 
		 TeamResponsible text, 
		 Type text,
		 FaceOffWinnerTeam text,
		 FaceOffLocation text,
		 FaceOffWinnerNumber text,
		 FaceOffWinnerName text,
		 FaceOffLoserNumber text,
		 FaceOffLoserName text,
		 ShooterNumber text,
		 ShooterName text,
		 ShotType text,
		 ShotDistance text,
		 StoppageReason text,
		 OffenderNumber text,
		 OffenderName text,
		 OffenceType text,
		 PenaltyLength text,
		 ScorerNumber text,
		 ScorerName text,
		 FirstAssistNumber text,
		 FirstAssistName text,
		 SecondAssistNumber text,
		 SecondAssistName text,
		 GoalShotType text,
		 GoalShotLength text,
		PlusPlayerOneNumber text,
		PlusPlayerTwoNumber text,
		PlusPlayerThreeNumber text,

		PlusPlayerFourNumber text,
		PlusPlayerFiveNumber text,
		PlusPlayerSixNumber text, 
		PlusPlayerOneName text, 
		PlusPlayerTwoName text, 
		PlusPlayerThreeName text,
		 
		PlusPlayerFourName text,
		PlusPlayerFiveName text,
		PlusPlayerSixName text, 
		PlusTeam text,
		MinusPlayerOneNumber text,
		MinusPlayerTwoNumber text,
		MinusPlayerThreeNumber text,

		MinusPlayerFourNumber text,
		MinusPlayerFiveNumber text,
		MinusPlayerSixNumber text, 
		MinusPlayerOneName text, 
		MinusPlayerTwoName text, 
		MinusPlayerThreeName text,

		MinusPlayerFourName text,
		MinusPlayerFiveName text,
		MinusPlayerSixName text, 
		MinusTeam text
		 );''')

	for j in range(len(Event)):

		c.execute("INSERT INTO NHLData VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
		(Season[j], 
		GameNumber[j], 
		EventIndex[j], 
		Period[j], 
		TimeOfEvent[j], 
		Event[j], 
		TeamResponsible[j], 
		Type[j],
		FaceOffWinnerTeam[j],
		FaceOffLocation[j],
		FaceOffWinnerNumber[j],
		FaceOffWinnerName[j],
		FaceOffLoserNumber[j],
		FaceOffLoserName[j],
		ShooterNumber[j],
		ShooterName[j],
		ShotType[j],
		ShotDistance[j],
		StoppageReason[j],
		OffenderNumber[j],
		OffenderName[j],
		OffenceType[j],
		PenaltyLength[j],
		ScorerNumber[j],
		ScorerName[j],
		FirstAssistNumber[j],
		FirstAssistName[j],
		SecondAssistNumber[j],
		SecondAssistName[j],
		GoalShotType[j],
		GoalShotLength[j],
		PlusPlayerOneNumber[j],
		PlusPlayerTwoNumber[j],
		PlusPlayerThreeNumber[j],

		PlusPlayerFourNumber[j],
		PlusPlayerFiveNumber[j],
		PlusPlayerSixNumber[j],
		PlusPlayerOneName[j],
		PlusPlayerTwoName[j],
		PlusPlayerThreeName[j],

		PlusPlayerFourName[j],
		PlusPlayerFiveName[j],
		PlusPlayerSixName[j], 
		PlusTeam[j],
		MinusPlayerOneNumber[j],
		MinusPlayerTwoNumber[j],
		MinusPlayerThreeNumber[j],

		MinusPlayerFourNumber[j],
		MinusPlayerFiveNumber[j],
		MinusPlayerSixNumber[j], 
		MinusPlayerOneName[j], 
		MinusPlayerTwoName[j], 
		MinusPlayerThreeName[j],

		MinusPlayerFourName[j],
		MinusPlayerFiveName[j],
		MinusPlayerSixName[j], 
		MinusTeam[j]
		))

	conn.commit()
	conn.close()


