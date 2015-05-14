def mainC(int size):
	cdef int tot = 1
	cdef int num = 3
	cdef int diff
	while num <= (size):
		diff = num - 1
		tot += 4*(num**2) - (6 * diff) 
		num += 2
	return tot
