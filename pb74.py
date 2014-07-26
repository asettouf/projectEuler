def factorial(n):
	if (n <1) :
		return 1
	else:
		ret = n*factorial(n-1)
		return ret
	

def sumOfFactorials(n): 
	buff = str(n)
	res = 0
	for char in buff:
		res += factorial(int(char))
	return res

def isTermInList(l,term):
	#print "list : " +str(l)
	#print "term : " + str(term)
	if (term in l):
		return True
	else:
		return False
		
MAX_RANGE = 1000000
def findLongestChains():
	listTemp = []
	counter = 0
	buff = 0
	for i in range(2, MAX_RANGE):
		listTemp.append(i)
		buff = sumOfFactorials(i)
		while(not (isTermInList(listTemp,buff))):
			
			listTemp.append(buff)
			buff = sumOfFactorials(buff)
			if(len(listTemp) > 59):
				break
		if (len(listTemp) == 60):
			counter += 1
		
		#print listTemp			
		listTemp = []
	return counter
	
print (findLongestChains())