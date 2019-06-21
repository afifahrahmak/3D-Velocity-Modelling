import mod_LatLongUTMconversion

def convertMultip(X, Y, Z, V, m):
	tempX = X
	tempY = Y
	tempZ = Z
	X = []
	Y = []
	Z = []
	for i in range(0, len(tempX)):
		X.append(float(tempX[i])*V)

	for i in range(0, len(tempY)):
		Y.append(float(tempY[i])*V)

	for i in range(0, len(tempZ)):
		Z.append(float(tempZ[i])*V*m)

	return X, Y, Z

def central(X, Y):
	tempX = 0
	tempY = 0
	for i in range(len(X)):
		tempX += X[i]
		tempY += Y[i]
	cenX = tempX/len(X)
	cenY = tempY/len(Y)

	return cenX, cenY

def corConv(X, Y):
	lat, longi = mod_LatLongUTMconversion.UTMtoLL(23, Y, X, '48M')
	return lat, longi

def dim(X, Y, Z, cenX, cenY):
	tempX = X
	tempY = Y
	tempZ = Z
	X = []
	Y = []
	Z = []
	for i in range(0, len(tempX)):
		X.append(tempX[i]*1000+cenX)

	for i in range(0, len(tempY)):
		Y.append(tempY[i]*1000+cenY)

	for i in range(0, len(tempZ)):
		Z.append(tempZ[i]*1000)
	
	return X, Y, Z