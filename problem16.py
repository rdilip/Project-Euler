def power(a,b):
	num = a
	for i in xrange(2,b+1):
		num = num * a
	return num
def digitSum(num):
	return sum([int(i) for i in list(str(num))])
print power(2,1000)
print digitSum(power(2,1000))
