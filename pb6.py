def sumOfSquare(end):
	sumOf = 0
	ofSum = 0
	for i in range(1,end +1):
		sumOf += i*i
		ofSum += i
	ofSum *= ofSum
	res = ofSum - sumOf
	return res

a = sumOfSquare(100)

print a