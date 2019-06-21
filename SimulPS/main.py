import simulps_to_earthq
import simulps_to_stasions
import simulps_to_velocity
import simulps_to_cal

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

	# create earthq data file -------------------------------------------
	fileOpen = 'dataCatalog2014.txt'
	fileSave = 'earthq.dat'

	no, eventID, staEq, arrP, pmP, ieP, arrS, ieS, Date, year, month, day, hour, minute, second, Tres, eqX, eqY, eqZ, errS, errX, errY, errZ, latDegEq, latMinEq, longDegEq, longMinEq = simulps_to_earthq.readData(fileOpen)
	simulps_to_earthq.writeData(fileSave, no, eventID, staEq, arrP, pmP, ieP, arrS, ieS, Date, year, month, day, hour, minute, second, Tres, eqX, eqY, eqZ, errS, errX, errY, errZ, latDegEq, latMinEq, longDegEq, longMinEq)

	# create stations data file -----------------------------------------
	fileOpen = 'dataSta2014.txt'
	fileSave = 'stations.dat'

	sta, latDegSta, latMinSta, longDegSta, longMinSta, ElevationSta, staY, staX = simulps_to_stasions.readData(fileOpen)
	cenX, cenY = simulps_to_stasions.writeData(fileSave, sta, latDegSta, latMinSta, longDegSta, longMinSta, ElevationSta, staY, staX)

	# create velocity data file -----------------------------------------
	fileOpen = 'dataVel.txt'
	fileSave = 'velocity.dat'

	# dimXd = [-200.8, -18.2, -15.6, -13.0, -10.4, -7.8, -5.2, -2.6, 0.0, 2.6, 5.2, 7.8, 10.4, 13.0, 15.6, 18.2, 200.8]
	# dimYd = [-200.8, -18.2, -15.6, -13.0, -10.4, -7.8, -5.2, -2.6, 0.0, 2.6, 5.2, 7.8, 10.4, 13.0, 15.6, 18.2, 200.8]
	dimXd = [-200.8, -13.0, -10.4, -7.8, -5.2, -2.6, 0.0, 2.6, 5.2, 7.8, 10.4, 13.0, 200.8]
	dimYd = [-200.8, -18.2, -15.6, -13.0, -10.4, -7.8, -5.2, -2.6, 0.0, 2.6, 5.2, 7.8, 10.4, 13.0, 15.6, 18.2, 200.8]
	
	# dimZd = [-30.0, 0.0, 0.5, 0.7, 1.0, 1.4, 1.9, 2.7, 3.8, 5.3, 7.4, 10.3, 20.5]


	# dimXd = [-200.0, -20.0, -12.0, -10.0, -8.0, -6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 20.0, 200.0]
	# dimYd = [-200.0, -20.0, -12.0, -10.0, -8.0, -6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 20.0, 200.0]
	# dimZd = [-40.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 17.0, 40.0]
	dimZd = [-100.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 20.0, 200.0]

	eqX, eqY, eqZ = simulps_to_cal.convertMultip(eqX, eqY, eqZ, 1000, 1) # convert 
	staX, staY, staZ = simulps_to_cal.convertMultip(staX, staY, ElevationSta, 1000, -1) # convert 
	dimX, dimY, dimZ = simulps_to_cal.dim(dimXd, dimYd, dimZd, cenX, cenY)
	
	simulps_to_velocity.plotXY(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ)
	simulps_to_velocity.plotXZ(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ)
	simulps_to_velocity.plotYZ(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ)

	Vp, VpVs = simulps_to_velocity.readData(fileOpen)
	simulps_to_velocity.writeData(fileSave, 1.0, dimXd, dimYd, dimZd, Vp, VpVs)
	plt.show()

	# create control data file -----------------------------------------

	neqs = 104
	nsht = 0
	nbls = 0
	wtsht = 0
	kout = 2
	kout2 = 0
	kout3 = 0
	
	nitloc = 5
	wtsp = 1
	eigtol = 0.05
	rmscut = 0.01
	zmin = -1
	dxmax = 0.1
	rderr = 0.01
	ercof = 0
	
	hitct = 35
	dvmpx = 0.05
	dvsmx = 0.05
	idmp = 0
	vpdmp = 10
	vpvsdmp = 10
	stadmp = 99
	stepl = 0.5
	
	ires = 1
	i3d = 3
	nitmax = 2
	snrmct = 0.001
	ihomo = 1
	rmstop = 0.001
	ifixl = 0
	
	deltl = 5
	delt2 = 25
	reil = 0.1
	res2 = 1
	rei3 = 2
	
	ndip = 9
	iskip = 2
	scale1 = 2
	scale2 = 2
	
	xfax = 1.2
	tlim = 0.001
	nitpb1 = 15
	nitpb2 = 15
	
	iusep = 1
	iuses = 1
	invdel = 1
