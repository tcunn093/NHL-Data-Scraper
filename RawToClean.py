from directoryref import HTMLReportDirectory
import re

#Open the textfile and designate each line as an entry in a list
textlist = open(HTMLReportDirectory + "\\2003-2004\\20001.txt", "r").read().splitlines()

#Remove every instance in the list that is contained within "<" and ">"
textlist = filter(None,[re.sub('<[^>]+>', '', i) for i in textlist])

#Remove any instance in the list after '<!--', and also remove anything that contains only empty space 
textlist = [x for x in textlist if textlist.index(x) < textlist.index('<!--') and not x.isspace()]

for l in textlist:
	print l

#Find hyphenLine in textfile and convert it to a single string
hyphenLine = "".join([x for x in textlist if not x.find('-') ])

#Count the spaces up to the next column and append the number of spaces to a list
i = 0
columnwidths = []
while i < len(hyphenLine) - 1:
 	if hyphenLine[i] + hyphenLine[i+1] == " -":
 		columnwidths.append(i+1)

 	i += 1
columnwidths = [0] + columnwidths
print columnwidths
copyrightLineIndex = textlist.index("".join([x for x in textlist if "Copyright" in x ]))
hyphenLineIndex = textlist.index(hyphenLine)

def indexOfFirstCharacter(s):
	return len(s) - len(s.lstrip())



EventIndex = []
Period = []
TimeOfEvent = []
Event = []
TeamResponsible = []
Type = []
Description = []

Data = [EventIndex, Period, TimeOfEvent, Event, TeamResponsible, Type, Description]

i = hyphenLineIndex + 1
while i < copyrightLineIndex:
	if indexOfFirstCharacter(textlist[i]) <= 4:
		for j in range(len(Data) - 1):
			Data[j].append(textlist[i][columnwidths[j]:columnwidths[j+1]])
			print Data[j]

	#print textlist[i]
	i += 1



#hyphenLine = [len(x) for x in hyphenLine]
#print hyphenLine








