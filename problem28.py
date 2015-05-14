def main(size):
	tot = 1
	num = 3
	while num <= (size):
		diff = num - 1
		tot += 4*(num**2) - (6 * diff) 
		num += 2
	return tot

