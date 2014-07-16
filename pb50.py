import math

def constructListOfPrime(lim):
	pp = 2
	ps = [pp]
	toAdd = False
	while pp < lim:
		pp += 1
		toAdd = True
		for a in ps:
			if a > math.sqrt(pp):
				break
			if pp%a == 0:
				toAdd = False
				break		
		if toAdd:
			ps.append(pp)
	return ps

def lengthSumOfPrime (primeList, prime):
	temp = 0
	count = 0
	#print primeList
	for pp in primeList:
		#print temp
		temp+= pp
		count+= 1
		if temp == prime:
			#print prime
			return count
		if temp > prime:
			break
	return 0

SIZE_PRIME = 1000000	
def findLongestLength():
	primeList = constructListOfPrime(SIZE_PRIME)
	#print primeList
	max = 0
	counter = 1
	for i in primeList[len(primeList) - 1000 : -1]:
		for j in range(0,counter):
			liTmp = primeList[j:counter]
			if (len(liTmp) < max +1):
				break
			buff = lengthSumOfPrime(liTmp, i)
			if buff > max:
				print i
				#print max
				#print i
				res = i
				max = buff			
		counter += 1
	return res			
	
print str(findLongestLength())


#Not a good script, execution time is too long if we check everything,
#thus we select an arbitrary subset of all primes that contains one prime at least
#under the (correct) assumption that the function that returns the max length
#is always growing, simply meaning that a subset containing at least the last value correct
#that is a prime which is a sum of consecutive primes, returns the correct result