import time
def digit_power(num):
	tot = 0
	temp = num
	while temp >= 1:
		tot += (temp % 10)**5
		temp = (temp - (temp % 10)) / 10
	if tot == num:return True
	else:return False
def sum_digit_power(limit):
	tot = 0
	for i in xrange(2,limit):
		if digit_power(i):tot += i
	return tot
start = time.time()
result = sum_digit_power(355000)
elapsed = time.time() - start
print "The result is %d, and it took %f seconds to find it." % (result, elapsed)
