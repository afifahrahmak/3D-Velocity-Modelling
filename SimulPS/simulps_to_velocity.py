import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm

def plotXY(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ):
	
	xx, yy = np.meshgrid(dimX, dimY)
	v = np.zeros_like(xx)+3

	plt.figure('XY')
	plt.pcolor(xx,yy,v, norm=LogNorm(vmin=0.1, vmax=1000), cmap=cm.jet_r, edgecolor='b')
	plt.plot(eqX, eqY, 'bo', markersize=4)
	plt.plot(staX, staY, 'r*')


def plotXZ(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ):
	
	xx, zz = np.meshgrid(dimX, dimZ)
	v = np.zeros_like(xx)+3

	plt.figure('XZ')
	plt.pcolor(xx,zz,v, norm=LogNorm(vmin=0.1, vmax=1000), cmap=cm.jet_r, edgecolor='b')
	plt.plot(staX, staZ, 'r*', markersize=4)
	plt.plot(eqX, eqZ, 'bo', markersize=4)
	plt.gca().invert_yaxis()

def plotYZ(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ):
	
	yy, zz = np.meshgrid(dimY, dimZ)
	v = np.zeros_like(yy)+3

	plt.figure('YZ')
	plt.pcolor(yy, zz, v, norm=LogNorm(vmin=0.1, vmax=1000), cmap=cm.jet_r, edgecolor='b')
	plt.plot(staY, staZ, 'r*', markersize=4)
	plt.plot(eqY, eqZ, 'bo', markersize=4)
	plt.gca().invert_yaxis()

def writeData(file, s, dimX, dimY, dimZ, Vp, VpVs):
	f = open(file,'w')
	f.write('%4.1f%3i%3i%3i\n' % (s, len(dimX), len(dimY), len(dimZ)))
	
	for i in range(0, len(dimX)):
		if i != len(dimX)-1:
			f.write('%6.1f' % (dimX[i]))
		else:
			f.write('%6.1f\n' % (dimX[i]))

	for i in range(0, len(dimY)):
		if i != len(dimY)-1:
			f.write('%6.1f' % (dimY[i]))
		else:
			f.write('%6.1f\n' % (dimY[i]))

	for i in range(0, len(dimZ)):
		if i != len(dimZ)-1:
			f.write('%6.1f' % (dimZ[i]))
		else:
			f.write('%6.1f\n' % (dimZ[i]))

	f.write('%3i%3i%3i\n' % (0, 0, 0))

	for k in range(0, len(dimZ)):
		for j in range(0, len(dimY)):
			for i in range(0, len(dimX)):
				if i != len(dimX)-1:
					f.write('%5.2f' % (Vp[k]))
				else:
					f.write('%5.2f\n' % (Vp[k]))

	for k in range(0, len(dimZ)):
		for j in range(0, len(dimY)):
			for i in range(0, len(dimX)):
				if i != len(dimX)-1:
					f.write('%5.2f' % (VpVs[k]))
				else:
					f.write('%5.2f\n' % (VpVs[k]))

def readData(file):
	f = open(file,'r')
	readD = f.readline()

	Vp = []
	VpVs = []

	while True:
		readD = f.readline()
		readDList = readD.split()
		print

		if readD == '':
			break
		Vp.append(float(readDList[0]))
		VpVs.append(float(readDList[1]))


	return Vp, VpVs

if __name__ == '__main__':

	dimX = [590000, 740000, 770000, 775000, 778000, 781000, 784000, 787000, 790000, 793000, 796000, 799000, 802000, 805000, 810000, 840000, 990000]
	dimY = [9000000, 9150000, 9180000, 9185000, 9188000, 9191000, 9194000, 9197000, 9200000, 9203000, 9206000, 9209000, 9212000, 9215000, 9220000, 9250000, 9400000]
	dimZ = [-500, 0, 2000, 2100, 2520, 3024, 3628.8, 4354.56, 5225.472, 6270.5664, 7524.67968, 9029.615616]

	eqX = [792260.882, 794209.882, 799245.882, 795263.882, 802623.882, 798445.882, 788841.882, 795288.882, 800362.882, 795906.882, 791455.882, 799339.882, 793818.882, 793778.882, 798683.882, 793008.882, 797571.882, 791120.882, 798767.882, 799093.882, 799713.882, 801496.882, 789836.882, 798867.882, 788919.882, 789599.882]
	eqY = [9195849.038, 9199361.038, 9195985.038, 9196846.038, 9200369.038, 9199230.038, 9192921.038, 9198786.038, 9192110.038, 9195498.038, 9199936.038, 9196765.038, 9200813.038, 9199593.038, 9194390.038, 9196056.038, 9195701.038, 9203844.038, 9195373.038, 9194477.038, 9193872.038, 9201907.038, 9202554.038, 9195548.038, 9202413.038, 9203631.038]
	eqZ = [-918.000, 8044.000, 3049.000, 3126.000, 3576.000, 3171.000, 3127.000, 3075.000, -1970.000, 3095.000, 2909.000, 3174.000, 3003.000, 3008.000, 2504.000, 3017.000, 3031.000, 3023.000, 2606.000, 2738.000, 2999.000, 6728.000, 3000.000, 3008.000, 3114.000, 4340.000]

	staX = [790965.1709, 776934.882, 804692.3673, 800942.4138, 802610.5547, 791756.1543]
	staY = [9202705.27, 9209678.038, 9191799.973, 9191169.831, 9185670.192, 9217297.483]
	staZ = [-1847, -1341, -1625, -2273, -1496, -1062]

	plotXY(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ)
	plotXZ(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ)
	plotYZ(dimX, dimY, dimZ, eqX, eqY, eqZ, staX, staY, staZ)


	plt.show()
















# x = [590000, 740000, 770000, 775000, 778000, 781000, 784000, 787000, 790000, 793000, 796000, 799000, 802000, 805000, 810000, 840000, 990000]
# z = [-500, 0, 2000, 2100, 2520, 3024, 3628.8, 4354.56, 5225.472, 6270.5664, 7524.67968, 9029.615616]


# # eqX = [814231]
# # eqY = [9240795]

# eqX = [792260.882, 794209.882, 799245.882, 795263.882, 802623.882, 798445.882, 788841.882, 795288.882, 800362.882, 795906.882, 791455.882, 799339.882, 793818.882, 793778.882, 798683.882, 793008.882, 797571.882, 791120.882, 798767.882, 799093.882, 799713.882, 801496.882, 789836.882, 798867.882, 788919.882, 789599.882]
# eqZ = [-918.000, 8044.000, 3049.000, 3126.000, 3576.000, 3171.000, 3127.000, 3075.000, -1970.000, 3095.000, 2909.000, 3174.000, 3003.000, 3008.000, 2504.000, 3017.000, 3031.000, 3023.000, 2606.000, 2738.000, 2999.000, 6728.000, 3000.000, 3008.000, 3114.000, 4340.000]

# staX = [790965.1709, 776934.882, 804692.3673, 800942.4138, 802610.5547, 791756.1543]
# staZ = [-1847, -1341, -1625, -2273, -1496, -1062]


# xx, zz = np.meshgrid(x, z)
# v = np.zeros_like(xx)+3

# plt.figure(2)
# plt.pcolor(xx,zz,v, norm=LogNorm(vmin=0.1, vmax=1000), cmap=cm.jet_r, edgecolor='b')

# # # plt.colorbar()
# plt.plot(staX, staZ, 'r*')
# plt.plot(eqX, eqZ, 'bo')
# plt.gca().invert_yaxis()
# plt.show()


