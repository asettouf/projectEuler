import math

def pentagonalRes(rank):
	P = (rank*(3*rank - 1))/2
	return P
def findPentagonalRank(P):
	delta = 1 + 4*3*2*P 
	x1 = (1 - math.sqrt(delta))/6
	x2 = (1 + math.sqrt(delta))/6
	rank = max(x1,x2)
	if (rank.is_integer()):
		return int(rank) + 1
	else:
		return -1

def checkPentagonal(rank1, rank2):
	Px = pentagonalRes(rank1)
	Py = pentagonalRes(rank2)
	sumPent = Px + Py
	rankSum = findPentagonalRank(sumPent)
	diffPent = abs(Px - Py)
	if rankSum == -1:
		return 0
	listPent = []
	for i in range(1, rankSum):
		listPent.append(pentagonalRes(i))
	if (sumPent in listPent and diffPent in listPent):
		print str(rank1)
		print str(rank2)
		print str(diffPent)
		return 1
	else:
		return 0
		
for i in range(1,10000):
	for j in range(1,10000):
		checkPentagonal(i,j)
		

#Very interesting problem showing that there are few numbers whose sum and difference are pentagonals, 
#and it seems (of course it is no mathematical proof) that when the difference is pentagonal, 
#the difference is equal to a constant : 5482660 (to investigate!)