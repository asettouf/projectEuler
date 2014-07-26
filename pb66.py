import math
D = 1

def isSquare(n):
	i = 0
	while i < int(math.sqrt(n) + 1):
		if ( i*i == n):
			return True
	return False

#let's try the chakravala method!

def findLeastSquareOf(n, skipper = False, m = 0):
	buff = 0
	res = 0
	min = abs(1 -n)
	for i in range(2,n):
		buff = abs(i*i -n)
		if i == m:
			if skipper:
				skipper = False
				continue
		if min > buff:
			min = buff
			res = i
	return res

def findNextX(Xr, Yr, pr1, kr):
	return float((pr1*Xr + D*Yr))/(abs(kr))

	
def findNextY(Xr, Yr, pr1, kr):
	return float((pr1*Yr + Xr))/(abs(kr))
	
def findNextK (pr1, kr):
	return (p*p - D)/kr

def findNextP(pr, kr):
	old = findLeastSquareOf(D)
	while (math.fmod(float(pr+old)/kr, 1) != 0) :
		new = findLeastSquareOf(D, True, old)
		old = new	
	return old	

def runOneStep(p,k,X,Y):
	res = []
	pres = findNextP(p,k)
	kres = findNextK(pres,k)
	Xres = findNextX(X,Y,pres,k)
	Yres = findNextY(X,Y,pres,k)
	res.append(Xres)
	res.append(Yres)
	res.append(pres)
	res.append(kres)
	return res
	
def findLargestX():
	