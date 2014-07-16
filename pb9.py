def checkOrder(a,b,c):
	test1 = a < b
	test2 = b < c
	if (test1 and test2):
		return 1
	else:
		return 0
	
def checkSumSquare(a,b,c):
	sumSquare =  a*a + b*b
	if sumSquare == c*c:
		return 1
	else:
		return 0


def finder():
	for i in range(1, 1000):
		for j in range(i,1000):
			for k in range(j, 1000):
				if(i+j+k == 1000):
					if (checkOrder(i,j,k) and checkSumSquare(i,j,k)):
						return i*j*k
				

a = finder()

print a