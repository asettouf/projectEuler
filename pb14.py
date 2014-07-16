def addCollatzTerm(prev):
	res = 0
	if(prev%2 == 0):
		res = prev/2
	else:
		res = 3*prev +1
	return res
	
def chain():
	chain = []
	term = 0
	rank = 0
	buff = []
	i = 13
	while i < 1000000:
		if rank == 0:
			term = i
		else:
			term = addCollatzTerm(term)
		rank += 1
		#print term
		buff.append(term)
		
		if term == 1:
			chain.append(buff)
			rank = 0
			buff = []
			i += 1
	return chain
	
def findLongestChain(chain):
	res = chain[0]
	for i in chain: 
		if len(i) > len(res):
			res = []
			res = i
	return res

chain = chain()

res = findLongestChain(chain)

#print (chain)

print (len(res))