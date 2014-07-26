function sumOfSquare(ende)
	sumOf = 0
	ofSum = 0
	for i = 1:ende
		sumOf += i*i
		ofSum += i
	end	
	ofSum *= ofSum
	res = ofSum - sumOf
	return res
end

a = sumOfSquare(100)

print (a)