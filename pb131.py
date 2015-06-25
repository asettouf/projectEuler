#!/usr/bin/env python

import math

CEIL = 1000000

def findPrimeNumbers():
	k = 0
	vals = []
	vals.append(False)
	vals.append(False)
	for k in range(2, CEIL):
		vals.append(True)
	k = 0
	res = []
	for i in range(2, math.floor(math.sqrt(CEIL))):
		if vals[i]:
			num = i*i
			j = num
			p = 1
			while j < CEIL:
				vals[j] = False
				j = num + p*i
				p += 1
				#print(j)
	for k in range(2, CEIL):
		if vals[k - 2]:
			#print("yoho")
			res.append(k-2)
	return res
	
def findUniqueN(prime):
	#when solving the equation for a million, we find the equation below 
	#(for n^2+n^3p = k^3 p being prime needs to be a perfect cube) and the majorant to be 577
	for k in range(1,577):
		if (prime == (k+1)*(k+1)*(k+1) - k*k*k):
			return True
	return False

def main():
	primes = findPrimeNumbers()
	counter = 0
	for t in primes:
		tt = findUniqueN(t)
		if tt:
			counter += 1
			continue
	print(counter)
			

main()
