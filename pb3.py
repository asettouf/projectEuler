import math

def isprime(n):
   """Returns True if n is prime"""
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False

   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return False

      i += w
      w = 6 - w

   return True
   
def findLargestPrimeFactor(n):
	factor = n
	listPrime = []
	for i in range(1,int(math.sqrt(n))):
		if(isprime(i)):
			listPrime.append(i)
	res = 1
	
	for j in listPrime:
		if( math.fmod(float(factor)/j, 1) == 0):
			res = j
			factor = factor/j
	return res
	
print findPrimeFactor(600851475143)