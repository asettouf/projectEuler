def fact(n):
	if n < 1:
		return 1
	else:
		ret = n*fact(n-1)
		return ret
a = fact(100)

def sumOfIntegers(integer):
	temp = str(integer)
	res = 0
	for i in temp:
		print i
		res += int(i)
	return res

test = 100	
print(str(test) + " : " + str(sumOfIntegers(fact(test))))