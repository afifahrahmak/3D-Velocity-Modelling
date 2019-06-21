def readData(file):
	f = open(file,'r')
	readD = f.readline()
	
	no = []
	eventID = []
	sta = []
	arrP = []
	pmP = []
	ieP = []
	arrS = []
	ieS = []
	Date = []
	year = []
	month = []
	day = []
	hour = []
	minute = []
	second = []
	Tres = []
	eqX = []
	eqY = []
	eqZ = []
	errS = []
	errX = []
	errY = []
	errZ = []
	latDeg = []
	latMin = []
	longDeg = []
	longMin = []

	while True:
		readD = f.readline()
		readDList = readD.split()
		if readD == '':
			break
		
		no.append(readDList[0])
		eventID.append(readDList[1])
		sta.append(readDList[2])
		arrP.append(float(readDList[3]))
		pmP.append(readDList[4])
		ieP.append(readDList[5])
		arrS.append(float(readDList[6]))
		ieS.append(readDList[7])
		Date.append(readDList[8])
		year.append(readDList[9])
		month.append(readDList[10])
		day.append(readDList[11])
		hour.append(readDList[12])
		minute.append(readDList[13])
		second.append(float(readDList[14]))
		Tres.append(readDList[15])
		eqX.append(float(readDList[16]))
		eqY.append(float(readDList[17]))
		eqZ.append(float(readDList[18]))
		errS.append(readDList[19])
		errX.append(readDList[20])
		errY.append(readDList[21])
		errZ.append(readDList[22])
		latDeg.append(int(readDList[23]))
		latMin.append(float(readDList[24]))
		longDeg.append(int(readDList[25]))
		longMin.append(float(readDList[26]))

	return no, eventID, sta, arrP, pmP, ieP, arrS, ieS, Date, year, month, day, hour, minute, second, Tres, eqX, eqY, eqZ, errS, errX, errY, errZ, latDeg, latMin, longDeg, longMin


def writeData(file, no, eventID, sta, arrP, pmP, ieP, arrS, ie, Date, year, month, day, hour, minute, second, Tres, eqX, eqY, eqZ, errS, errX, errY, errZ, latDeg, latMin, longDeg, longMin):
	f = open(file,'w')
	k=0
	for i in range(0, len(no)):
		k+=1
		if no[i-1] != no[i]:
			if i == 0 and k != 0:
				f.write('%-2s%-2s%-2s %-2s%-2s %5.2f%3i %5.2f %3i %5.2f%7.2f%7.2f\n' % (year[i][2:], month[i], day[i], hour[i], minute[i], second[i], latDeg[i], latMin[i], longDeg[i], longMin[i], eqZ[i], 2.00))
			else:
				if k == 1:
					f.write('0     \n')
				else:
					f.write('\n0     \n')
				f.write('%-2s%-2s%-2s %-2s%-2s %5.2f%3i %5.2f %3i %5.2f%7.2f%7.2f\n' % (year[i][2:], month[i], day[i], hour[i], minute[i], second[i], latDeg[i], latMin[i], longDeg[i], longMin[i], eqZ[i], 2.00))
				k=1
		if (k%3) != 0:
			# f.write(str(k))
			f.write('%4s%2s%2s%6.2f%4s%2s%2s%6.2f' % (sta[i], 'P', '0',arrP[i]-second[i],sta[i], 'S', '0',arrS[i]-arrP[i]))
		else:
			f.write('%4s%2s%2s%6.2f%4s%2s%2s%6.2f\n' % (sta[i], 'P', '0',arrP[i]-second[i],sta[i], 'S', '0',arrS[i]-arrP[i]))
			# f.write(str(k)+'\n')
			k=0
	f.close()

	# f = open(file,'r')

if __name__ == '__main__':
	fileOpen = 'dataCatalog2014.txt'
	fileSave = 'earthq.dat'

	no, eventID, sta, arrP, pmP, ieP, arrS, ie, Date, year, month, day, hour, minute, second, Tres, eqX, eqY, eqZ, errS, errX, errY, errZ, latDeg, latMin, longDeg, longMin = readData(fileOpen)

	writeData(fileSave, no, eventID, sta, arrP, pmP, ieP, arrS, ie, Date, year, month, day, hour, minute, second, Tres, eqX, eqY, eqZ, errS, errX, errY, errZ, latDeg, latMin, longDeg, longMin)

