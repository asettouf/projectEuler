def checkPalind(num): 
	buff=""
	tt = str(num)
	for i in tt:
		buff+= i
	buff = int(buff)
	if buff == num:
		return True
	else:
		return False

def reverseNumber(num):
	tt = str(num)
	res = int(tt[::-1])
	return res


		