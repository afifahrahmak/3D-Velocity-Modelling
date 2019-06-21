import simulps_to_cal
import matplotlib.pyplot as plt
import math

def readData(file):
	f = open(file,'r')
	readD = f.readline()
	
	sta = []
	latDeg = []
	latMin = []
	longDeg = []
	longMin = []
	Elevation = []
	Y = []
	X = []
	

	while True:
		readD = f.readline()
		readDList = readD.split()
		if readD == '':
			break
		sta.append(readDList[0])
		latDeg.append(int(readDList[1]))
		latMin.append(float(readDList[2]))
		longDeg.append(int(readDList[3]))
		longMin.append(float(readDList[4]))
		Elevation.append(float(readDList[5]))
		Y.append(float(readDList[6]))
		X.append(float(readDList[7]))

	return sta, latDeg, latMin, longDeg, longMin, Elevation, Y, X


def writeData(file, sta, latDeg, latMin, longDeg, longMin, Elevation, Y, X):
	UTMcenX, UTMcenY = simulps_to_cal.central(X, Y)
	cenY, cenX = simulps_to_cal.corConv(UTMcenX*1000, UTMcenY*1000)

	centLatDeg = (math.trunc(cenY)*-1)
	centLatMin = (cenY*-1 - centLatDeg) *60

	centLongDeg = (math.trunc(cenX))
	centLongMin = (cenX - centLongDeg) * 60

	f = open(file,'w')
	f.write('%3s %5.2f %3s %5.2f %7.2f \n' % (centLatDeg, centLatMin, centLongDeg, centLongMin, 0))
	f.write('%3s \n' % (str(len(sta))))
	for i in range(0, len(sta)):
		f.write('  %4s%2i %5.2f%4i %5.2f%5i %4.2f %4.2f %1i  \n' % (sta[i], latDeg[i], latMin[i], longDeg[i], longMin[i],Elevation[i]*-1000,0,0,0))

	return UTMcenX*1000, UTMcenY*1000

if __name__ == '__main__':
	fileOpen = 'dataSta2014.txt'
	fileSave = 'stasions.dat'

	sta, latDeg, latMin, longDeg, longMin, Elevation, Y, X = readData(fileOpen)

	writeData(fileSave, sta, latDeg, latMin, longDeg, longMin, Elevation, Y, X)


