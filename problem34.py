def factorial(num):
	if num == 1 or num == 0:
		return 1
	else: 
		return num * factorial(num - 1)

def main(limit):
	facts = map(factorial,range(0,10))
	total_sum = 0
	for num in xrange(10,limit):
		tot = 0
		temp = num
		while temp > 0:
			tot += facts[temp % 10]
			temp /= 10
		if tot == num:
			total_sum += num
	return total_sum
