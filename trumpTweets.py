#nightTime defined as 6:00 PM to 6:00 AM

#data from http://www.trumptwitterarchive.com/archive

import datetime 

def readFile(path):
	with open(path, "rt") as f:
		return f.read()

def dayOrNight(time):
	time = datetime.datetime.strptime(time, '%H:%M:%S')
	day = datetime.datetime.strptime("06:00:00", '%H:%M:%S')
	night = datetime.datetime.strptime("18:00:00", '%H:%M:%S')
	if (time <= day):
		return "night"
	elif (time > night):
		return "night"
	else: return "day"

def makeList():
	finalList = []
	data = readFile("trumpTweets.txt")
	lastIndex = 6247457
	index = 0
	while index < lastIndex:
		index = data.find("\nTwitter", index)
		while data[index] != ",":
			index += 1
		index += 1
		endingIndex = index
		while data[endingIndex] != ",":
			endingIndex += 1
		timeStart = data.find("-20", endingIndex)
		if data[timeStart+3] == "-":
			timeStart += 3
		timeStr = data[timeStart+6:timeStart+14]
		timeStr = dayOrNight(timeStr)

		finalList.append([data[index:endingIndex],timeStr])
	return finalList
print(len(makeList()))