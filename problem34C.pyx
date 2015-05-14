cdef factorial(int num):
	if num == 1 or num == 0:
		return 1
	else: 
		return num * factorial(num - 1)

def mainC(int limit):
	cdef: 
		int *facts = [1,1,2,6,24,120,720,5040,40320,362880]
		int total_sum = 0
		int	tot = 0
		int temp
	for num in xrange(10,limit):
		tot = 0
		temp = num
		while temp > 0:
			tot += facts[temp % 10]
			temp /= 10
		if tot == num:
			total_sum += num
	return total_sum
