def cdigit_power(num):
	cdef int tot = 0
	cdef int temp = num
	while temp >= 1:
		tot += (temp % 10)**5
		temp = (temp - (temp % 10)) / 10
	if tot == num:return True
	else:return False
def digit_power(num):
	return cdigit_power(num)
cdef int csum_digit_power(limit):
	cdef int tot = 0
	for i in xrange(2,limit):
		if cdigit_power(i):
			tot += i
	return tot
def sum_digit_power(limit):
	return csum_digit_power(limit)